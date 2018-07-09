## 학습 전에 제대로 돌아가는지 확인하는 팁
	1. 맞는 손실함수를 찾아야
		a. 기대한 만큼의 loss function 값이 실제로 나오는지 확인해야함
		b. (ex cifar-10 데이터에서 softmax 쓰면 손실함수를 2.302로 기대할 수 있음(-ln(0.1)=2.302 / 각 클래스에 확률이 0.1로 분산)
	2. 정규화 강도를 올릴수록 손실 함수 값이 올라가야 함
	3. 자료의 작은 부분 집합으로 과적합 해봐야
		a. 20개 자료정도로 0cost 가 나오는지 확인해봐야해(정규화 강도를 0으로 해 놓고)
		b. 작은 자료에서 확인이 제대로 안되면 전체 과정이 무가치함
## 학습 과정 확인(babysitting the learning process)

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
	• Batch 는 한번에 다 network 태워서 learning 시키는 것
	• Stochastic 은 데이터중 일부씩을 뽑아서 계산후 back prop로 w update 과정을 반복해서 w 를 완성시킴
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
