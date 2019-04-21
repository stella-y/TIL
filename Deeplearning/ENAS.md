## ENAS(Efficient Neural Architecture Search via Parameter Sharing)
### motivation
* NAS(Neural architecture search with reinforcement learning(2017))
	- controller 통해서 architecture 학습
	- perplexity 같은걸 reward function 으로 정의
	- architecture 학습 --> training/perplexity 확인으로 reward 측정 --> architecture 학습의 과정을 반복
	* controller 를 rnn으로 구성
		* 각 layer 별로, architecture 의 특성을 하나씩 학습이 가능하게 만들어 둠
		* method
			* 전체적인 Conv net 의 architecture 는 manually pretrained
			* normal cell
				* 동일한 dimension 에 대한 feature map 을 return 하는 convolution cell
			* reduction cell
				* factor of two 만큼 줄어든 height 와 width 의 feature map 을 return 하는 convoluition cell
		* 결국 node 들을 정해놓고, 이것들의 연결을 꼽는 방향인 것
--> 이런 논문예시들이 있으나 resource 가 너무 많이 들더라
--> 왜 이렇게 오래 걸릴까 / child model 에 대해서 전체 학습을 거듭해야해서 너무 오래걸린다
--> weight 학습을 끝내놓고도, 이걸 다 버리고 accuracy 만 쓰는게 낭비라는 생각


### main idea
* child model 이 weight 를 share 하게 함(transfer learning 개념을 쓴건데,,, 사실 논리적으로 완벽히 와닿지는 않아서... 근데 practical 하게 했더니 잘 되더라...)
* 이렇게 했더니 gpu 1개에서 16시간만에 학습 되더라...
* DAG 를 만드는 문제로 생각
	* Recurrent Cell을 새로 구성
		LSTM, GRU 는 결국 사람이 구성한거니 한계 존재하므로, 이런 구성까지 모델에 맡겨보자는 아이디어
		* 구성 방법
			* 첫번째 RNN 출력: 1번 노드의 연산 출력
			* 두번째 RNN 출력: 2번 노드의 입력 노드 출력
			* 세번째 RNN 출력: 2번 노드의 연산 출력
			* 네번째 RNN 출력: 3번 노드의 입력 노드 출력
			* 다섯번째 RNN 출력: 2번, 3번 노드의 연결 방법 출력
			* ...
* 학습방법
	* 각 노드들의 weight 를 share 함



