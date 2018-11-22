## Learning to Explain: An Information-Theoretic Perspective on Model Interpretation

코드 리뷰
``` python
def L2X(datatype, train = True): 
	x_train,y_train,x_val,y_val,datatype_val, input_shape = create_data(datatype, 
		n = int(1e6))
	 
	st1 = time.time()
	st2 = st1

	activation = 'relu' if datatype in ['orange_skin','XOR'] else 'selu'
	# P(S|X) 
	model_input = Input(shape=(input_shape,), dtype='float32') 

	net = Dense(100, activation=activation, name = 's/dense1',
		kernel_regularizer=regularizers.l2(1e-3))(model_input)
	net = Dense(100, activation=activation, name = 's/dense2',
		kernel_regularizer=regularizers.l2(1e-3))(net) 

	# A tensor of shape, [batch_size, max_sents, 100]
	logits = Dense(input_shape)(net) # sampling 결과
	# [BATCH_SIZE, max_sents, 1]  
	k = ks[datatype]; tau = 0.1
	samples = Sample_Concrete(tau, k, name = 'sample')(logits) # gumbel softmax 에서 확률 분포를 뽑아냄

	# q(X_S) 뽑아낸 sample 만 이용해서 다시 생성
	new_model_input = Multiply()([model_input, samples]) # 뽑아낸 것 * 뽑은 것(나머지것들이 없어짐)
	net = Dense(200, activation=activation, name = 'dense1',
		kernel_regularizer=regularizers.l2(1e-3))(new_model_input) 
	net = BatchNormalization()(net) # Add batchnorm for stability.
	net = Dense(200, activation=activation, name = 'dense2',
		kernel_regularizer=regularizers.l2(1e-3))(net)
	net = BatchNormalization()(net)
	# mlp

	preds = Dense(2, activation='softmax', name = 'dense4',
		kernel_regularizer=regularizers.l2(1e-3))(net) # binary classification(dimension이 2!!)
	model = Model(model_input, preds)

	if train: 
		adam = optimizers.Adam(lr = 1e-3)
		model.compile(loss='categorical_crossentropy',
					  optimizer=adam,
					  metrics=['acc']) 
		filepath="models/{}/L2X.hdf5".format(datatype)
		checkpoint = ModelCheckpoint(filepath, monitor='val_acc', 
			verbose=1, save_best_only=True, mode='max')
		callbacks_list = [checkpoint]
		model.fit(x_train, y_train, validation_data=(x_val, y_val),callbacks = callbacks_list, epochs=1, batch_size=BATCH_SIZE)
		st2 = time.time() 
	else:
		model.load_weights('models/{}/L2X.hdf5'.format(datatype), 
			by_name=True) 


	pred_model = Model(model_input, samples)
	pred_model.compile(loss=None,
				  optimizer='rmsprop',
				  metrics=[None]) 

	scores = pred_model.predict(x_val, verbose = 1, batch_size = BATCH_SIZE) 

	median_ranks = compute_median_rank(scores, k = ks[datatype],
		datatype_val=datatype_val)

	return median_ranks, time.time() - st2, st2 - st1


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()

	parser.add_argument('--datatype', type = str, 
		choices = ['orange_skin','XOR','nonlinear_additive','switch'], default = 'orange_skin')
	parser.add_argument('--train', action='store_true')

	args = parser.parse_args()

	median_ranks, exp_time, train_time = L2X(datatype = args.datatype, 
		train = args.train)
	output = 'datatype:{}, mean:{}, sd:{}, train time:{}s, explain time:{}s \n'.format( 
		args.datatype, 
		np.mean(median_ranks), 
		np.std(median_ranks),
		train_time, exp_time)

	print(output)

```

``` python
class Sample_Concrete(Layer):
	"""
	Layer for sample Concrete / Gumbel-Softmax variables. 
	"""
	def __init__(self, tau0, k, **kwargs): 
		self.tau0 = tau0
		self.k = k
		super(Sample_Concrete, self).__init__(**kwargs)

	def call(self, logits):   
		# logits: [BATCH_SIZE, d]
		logits_ = K.expand_dims(logits, -2)# [BATCH_SIZE, 1, d]

		batch_size = tf.shape(logits_)[0]
		d = tf.shape(logits_)[2]
		uniform = tf.random_uniform(shape =(batch_size, self.k, d), 
			minval = np.finfo(tf.float32.as_numpy_dtype).tiny,
			maxval = 1.0)

		gumbel = - K.log(-K.log(uniform)) # gumbal softmax 확률 추출
		noisy_logits = (gumbel + logits_)/self.tau0 # gumbal + logit
		samples = K.softmax(noisy_logits) # softmax 가져오고,
		samples = K.max(samples, axis = 1) # continuous 할 것

		# Explanation Stage output. --> 이 아래는 test 때
		threshold = tf.expand_dims(tf.nn.top_k(logits, self.k, sorted = True)[0][:,-1], -1)
		# output 중에서 가장 높은 확률을 갖는 k개의 pixel 값을 바로 return 함
		discrete_logits = tf.cast(tf.greater_equal(logits,threshold),tf.float32)
		
		return K.in_train_phase(samples, discrete_logits)

	def compute_output_shape(self, input_shape):
		return input_shape 

```