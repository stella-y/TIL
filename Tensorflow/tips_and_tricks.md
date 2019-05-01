## gpu 사용시(jupyter notebook keras tensorflow)
* jupyter notebook 은 물려있는 장비 전체의 메모리를 점유해버림
   * 장비 선택해두는게 필수적임
   ```python
   os.environ['CUDA_VISIBLE_DEVICES']="1" #장비번호 설정
   ```
   * 쓰는만큼 메모리주는것도 설정해둬야함
   ``` python
   import tensorflow as tf
   config=tf.ConfigProto()
   config gpu_options.allow_growth=True
   sess=tf.Session(config=config)
   import keras.backend.tensorflow_backend as K
   K.set_session(sess)
   ```
   * 장비를 진짜 여러개 쓰려면
   https://keras.io/utils/#multi_gpu_model 참고
   
## hyper-parameters
* Batch vs stochastic gradient descent
	* Batch 는 한번에 다 network 태워서 learning 시키는 것
	* Stochastic 은 데이터중 일부씩을 뽑아서 계산후 back prop로 w update 과정을 반복해서 w 를 완성시킴
* Learning rate 의 결정
	* Learning rate decay
		* 너무 커도, 작아도 문제
		* Rule of thumb : model 이 working 하지 않을 때에 learning rate 를 낮춰
			* 좋은   learning rate 의 rule
				* If steep : long steps
				* If plain : small steps
	* Random restart
		* Learning rate 조절 방법중 하나로 아무데서나 시작하는 random restart 를 반복할 수 있음
	* Momentum
		* 진행 하고 있던 힘(방향?)을 합쳐서 local min 에서도 더 진행함
