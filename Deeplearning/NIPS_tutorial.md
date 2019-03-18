## Unsupervised learning
### Introduction
* Types of learning
	* 
* Why learn without a teacher?

* transfer learning

* intelligence - cake
unsupervised learning - cake
supervised learning - icing on the cake
reinforcement learning - cherry on the cake
-- yann lecun
* Unsupervised learning
	* basic challenge - task 가 undefined
	* 다른 많은 태스크들을 아우를 수 있는 network 를 구성할 수 있게 하는 single task 를 잘 구성하는게 중요해짐
* density modeling
	* target 대신에 데이터 자체에 maximum likelihood 를 구함
	* True distribution 을 얻어내는걸 목표로 하게 됨
	* 데이터에 대한 모든 것을 학습하게 하고자 함


### Autoregressive models
* density modeling 이 필요하다면 어떤 모델을 사용해야하는지가 또 question 일 것
* 이때 쓸 수 있는 모델 중 하나가 autoregressive model
* time series 데이터, 시간순, 순서가 있는 뭔가에 대한 prediction 이면 이런 chain rule 기반으로 한 예측이 일반적일 것
--> autoregressive model 이 결국 이런것들을 neural net 에 적용한 것
* basic trick:
	* 고차원의 데이터를 sequence of small pieces 로 쪼개서, 각 piece 를 그 이전의 piece 들로 예측하는 것
	(작은 piece 로 쪼갠 것 만으로 여러 parameter 나 variable 을 고려하는 것에서는 벗어났다고 봐서 curse of dimensionality 는 극복했다고 봄)
* auto regressive model 에서의 three basic structure(winner 라고 부를 수 있을만 한 것들 세개)
	1. gated rnn (lstm, gru)
	2. masked convolutions (future state 가 past state에 영향을 줄 수 없도록 masked 한 것)
	3. transformer (convolution 이나 recursive state 가 완벽히 배제됨 / past 는 attention mechanism 에 의해서만 고려됨)
* 근데 위의 세개 중 어떤걸 선택하더라도 유사한 loss function 과 유사한 행위를 해야만 함
	* 과거의 정보를 network 에 high dimensional vector 로 embeds 시키고, 이를 output layer 로 보내서, prediction 함
* advantage
	1. simple - 
* disadvantage
	1. expensive - 병렬화로 training 은 완화할 수 있는데, 여전히 generation 은 순서대로 해야함
	2. order dependent - 
	3. 한 스텝 앞만을 예측해서 근시안적일수밖에 없음
* laugnage model
	* language model 은 전부 다 auto regressive model 일 수 밖에 없음 / 이전까지 나온 단어들로 그 다음을 예측하게 됨
	* 이 슬라이드에서는 color code 중 하나가 원래의 문장이고, 또 다른 하나가 기계가 생성한 문장임(이미 구분이 어려운 정도임)
* wavenets
	* 이전의 오디오 시그널로 그 다음의 시그널을 생성함
	* 꼭 텍스트 데이터가 들어가지 않더라도 babbling 이라도 한다더라
* pixel rnn
	* auto regressive model 의 형식을 이미지에 적용한 것
	* order 에 대한 정의가 중요해짐(raster scanning 이 일반적임)
	* 신기한 점은 rgb channel 의 256을 continuous 한 수로 보는 것 보다, 독립된 class 로 취급해서 softmax 로 prediction 을 하는게 성능이 더 좋더라는 점(가우시안 모델을 쓰는 것 보다 그냥을 쓰는게 더 낫더라)
	* 그냥 썼을 때는 예시로 보는 것 처럼 global structure 보다는 local structure 를 생성하는데에 더 특화되어있음을 알 수 있었음
	* 여기에 label 로서 컨디션을 준 다음부터는 global structure 를 보는 것 처럼 보임
	(condition 을 줬더니 log likelyhood 값이 크게 달라지지는 않았지만, 그 성능에 있어서는 확실히 달리지는게 보였음 --> density model 에 대한 argue 할 요소로 쓰여버림)
	* subsample pixel network - raster scan 대신에 pixel 들을 slice 해서 예측하는걸 시도해봄
* video pixel network(vpn)
	* 당연히 resolution 이 매우 낮을 것
* Handwriting synthesis
	* nostahgic 하게 handwriting sequence 를 generate
	* Autoregressive mixture models
		* 이전까지는 discrete 하게 해석했지만 continuous 하게 해석
		* 그 다음 step 이 등장할 xy coordinate 를 예측(그 다음으로 쓰여질 handwriting 이 어디로 향하게될지를 xy coordinate 로 예측하게 되는 것)


### Representation learning
* unsupervised learning 을 하는 건 결국 해석 



### Unsupervised reinforcement learning



