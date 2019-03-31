## Batch vs stochastic gradient descent
* Batch : 한번에 다 network 태워서 learning 시키는 것(epoch 한번 마다 w update)
* Stochastic : 데이터중 일부씩을 뽑아서 계산후 back prop로 w update 과정을 반복, w 를 완성시킴

## Learning rate 의 결정
* Learning rate decay
	* 너무 커도, 작아도 문제
	* Rule of thumb : model 이 working 하지 않을 때에 learning rate 를 낮추는 식으로 정한다!
		* 좋은   learning rate 의 rule
			* If steep : long steps
			* If plain : small steps
* Random restart
	* learning rate 에 대해 random 의 값을 반복해서 최적의 상태를 정함
* Momentum
	* 진행 하고 있던 힘(방향?)을 합쳐서 local min 에서도 더 진행함
	
## Deal with non linear data - regression 에 활용
* Piecewise linear function 방식으로…
	* 각 구간들을 linear function 으로 가정하여 regression 해가는 방식
	* relu로 activate 하고,
	* Classification 문제면 마지막에 sigmoid 로...
	![piecewise](images/3_1.png "piecewise")
	* Regression 으로 하고싶다면
		* Error function 을 (y-y^)^2
