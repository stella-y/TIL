## Optimization
1. Early Stopping
	* Epoch 을 거듭할수록 정확도는 증가하나 overfit 될 것
	* --> 이 그래프가 model complexity graph
	![model_complexity](image/Opt_1.png "model_complexity")
	* Testing error 가 감소할때까지만 gradient descent 를 돌려
2. Regularization
	* Coefficient 가 클 경우 실제 분리하게 되는 line 은 동일한데, error 가 적게 나오는 경우가 있음(sigmoid function 이 꾸겨져셔)
	* Penalize large weights
	![regularization](image/Opt_2.png "regularization")
	(위가 l1, 아래가 l2)
	* L1(sparse 해져) - good for feature selection(1아님 0으로 다 걸러짐)
	* L2 - 모델 트레이닝에 더 좋아(숫자가 다 남으니깐) 
3. Drop out
	* 노드 몇개만 강력하게 트레인 되서 이용될 수 있으니, epoch 마다 하나씩을 빼가면서 트레이닝 시켜봐 그런 다음 테스팅 할땐 다 활용

