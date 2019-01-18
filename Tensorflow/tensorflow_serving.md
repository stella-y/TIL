## Tensorflow serving
### Preperation - model serialize
* serving 에 태우려면 .checkpoint 파일만으론 안된다
* graph 와 variable, input output tensor 가 모두 정의된 serialized file 을 먼저 만들어야 함
--> serialized file(.pb 파일)
graph 형태 미리 확인한 후(graph.get_operations()), 거기에 알맞는 input, output tensor 를 가져와서 input, output 임을 명시해야 함


#### checkpoint 에서 graph 가져오기
```python
checkpoint = tf.train.latest_checkpoint(SAVE_PATH)
tf.reset_default_graph()
saver = tf.train.import_meta_graph(checkpoint + '.meta')
with tf.Session() as sess:
	graph=tf.get_default_graph()
    sess.run(tf.global_variables_initializer())
    #get input, output tensors
    input=graph.get_tensor_by_name('encode_ids:0') #input tensor 확인후 그 이름 넣는 것
    output=graph.get_tensor_by_name('encoder_out/thought_vectors:0') #output tensor 확인 후 그 이름 넣는 것
```

#### input, output tensor 가져와서 tensor info 생성
```python
model_input = tf.saved_model.utils.build_tensor_info(input)
model_output = tf.saved_model.utils.build_tensor_info(output)
```

#### signature define 후 builder 선언
```python
signature_definition = tf.saved_model.signature_def_utils.build_signature_def(
    inputs={'input': model_input},
    outputs={'output': model_output},
    method_name= tf.saved_model.signature_constants.PREDICT_METHOD_NAME)
builder=tf.saved_model.builder.SavedModelBuilder(SERVE_PATH)
```

#### builder 에 metagraph 와 variable 추가한 후 모델 save
```python
builder.add_meta_graph_and_variables(
    sess, [tf.saved_model.tag_constants.SERVING],
    signature_def_map={
        tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY : signature_definition
    })
builder.save()
```

#### 예시 코드
```python

g = tf.Graph()
with g.as_default():
  encoder = s2v_encoder.s2v_encoder(model_config)#encoder 파일에서 가져오면서 tensor 변형 있어서 이렇게 한것임 / 사실 그냥 checkpoint 파일에서 그냥 읽어오면 됨
  restore_model = encoder.build_graph_from_config(model_config)

with tf.Session() as sess:
    graph=g
    sess.run(tf.global_variables_initializer())
    #get input, output tensors
    encode_ids=graph.get_tensor_by_name('encode_ids:0')
    encode_mask=graph.get_tensor_by_name('encode_mask:0')
    enc=graph.get_tensor_by_name('encoder/thought_vectors:0')
    enc_out=graph.get_tensor_by_name('encoder_out/thought_vectors:0')

input_encode_ids=tf.saved_model.utils.build_tensor_info(encode_ids)
input_encode_mask=tf.saved_model.utils.build_tensor_info(encode_mask)
output_enc=tf.saved_model.utils.build_tensor_info(enc)
output_enc_out=tf.saved_model.utils.build_tensor_info(enc_out)

signature_definition = tf.saved_model.signature_def_utils.build_signature_def(
    inputs={'input_encode_ids': input_encode_ids, 'input_encode_mask': input_encode_mask},
    outputs={'output_enc': output_enc, 'output_enc_out' : output_enc_out},
    method_name= tf.saved_model.signature_constants.PREDICT_METHOD_NAME)

MODEL_NAME = 'model'
SUB_NAME='comment07'
VERSION = 1
SERVE_PATH = '/data1/comment_model/serve/{}_{}/{}'.format(SUB_NAME, MODEL_NAME, VERSION)

builder=tf.saved_model.builder.SavedModelBuilder(SERVE_PATH)

builder.add_meta_graph_and_variables(
    sess, [tf.saved_model.tag_constants.SERVING],
    signature_def_map={
        tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY : signature_definition
    })
builder.save()

```