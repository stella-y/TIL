## Batch size in deep learning
* batch : divide dataset into Number of Batches or sets or parts

* 대부분의 학습은 mini-batch stochastic gradient descent 기반으로 이뤄짐
* batch size 가 모델 학습에 끼치는 영향과 관련한 연구들이 진행중 --> 정확하게 밝혀진건 없지만 작은 batch size 사용하면 generalization performance 측면에서 긍정적임
* Gradient descent
	* gradient 의 반대방향으로 step size(learning rate) 만큼 parameter 를 업데이트해나가게 됨
* stochastic gradient descent
	* 한 iteration 에 하나의 example 만 사용함
	* iteration 계산은 훨신 빠른데, gradient 추정값이 너무 noisy 해짐
* mini-batch stochastic gradient descent
	* 매 iteration 당 적당한 크기의 minibatch 에 대한 gradient 를 사용함
	* batch size 가 클수록 gradient 가 정확해지지만, 한 iteration 에 대한 계산량은 늘어나게 됨
	* 근데 한 iteration 에서 각 example 에 대한 gradient 는 parallel 하게 계산이 가능해서 큰 batch 를 사용하면 multi-gpu 등 parallel computation 의 활용도를 높이고, 학습시간을 단축함

https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network