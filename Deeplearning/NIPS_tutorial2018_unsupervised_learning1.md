- nips tutorial 2018 자료에서 unsupervised learning 발표 요약

## Unsupervised learning
### Introduction
* Types of learning
	* Supervised, unsupervised, reinforcement learning 이런 식의 구분은 맞지 않다고 생각함
	* 2차원으로 주어진 데이터를 그대로 배우면 passive, agent 가 존재해서 agent 의 움직임에 따라서, 관찰하게 되는 데이터나 state 가 달라진다면 active
	* Teacher 로부터의 signal 이 있는가 없는가 
		* Supervised, unsupervised 는 명확할 것
		* 일반적인 rl 이라서 extrinsic 한 reward 를 얻으면 with teacher 인 것, 아니면 without teacher 인 것(explore 하거나, intrinsic motivation 을 이용하게 될 경우)
* Why learn without a teacher?
	* Target 이나 reward 를 정의하는게, 혹은 label을 만드는게 쉽지 않을 수 있음
	* Unsupervised 의 방식이 사람이 배우는 방식이다
	* 새로운 task 나 상황이 생겼을 때에 generalisation 이 가능해진당
* Transfer learning
	* Multi-task learning 이나 one shot learning
	* 하나의 task 에 대해서 학습을 해서 다른 task 에 그대로 활용하는 것
	* 만약에 하나의 언어에 대한 데이터가 엄청 모자라면 연관성이 있는 다른 데이터로 러닝 시켜서 쓰는 것(target 이 아니라 skill 을 학습시킨다고 볼 수있음)
	* 근데 당연한얘기지만 원하는 만큼 generalize 가 안됨

* intelligence - cake
	unsupervised learning - cake
	supervised learning - icing on the cake
	reinforcement learning - cherry on the cake
	-- yann lecun
	* --> 정보의 양이 그러하다 / 각 learning 방식에서 사용할 수 있게 되는 정보의 양이 이렇게나 불균형하다

* Unsupervised learning
	* basic challenge - task 가 undefined
	* 다른 많은 태스크들을 아우를 수 있는 network 를 구성할 수 있게 하는 single task 를 잘 구성하는게 중요해짐
* density modeling
	* target 대신에 데이터 자체에 maximum likelihood 를 구함
	* True distribution 을 얻어내는걸 목표로 하게 됨
	* 데이터에 대한 모든 것을 학습하게 하고자 함
* Where to look
	* 당연히 데이터에서 모든 것을 배우는게 비효율적일 것
	* 언젠가는 유용하게 쓰일 먼가를 뽑아낼 수는 없을까
* Problems with density modeling
	1. Curse of dimensionality - 오디오, 비디오 signal 에서 배워야하고, 이전까지는 몇개의 bit 만 학습하면 됐지만 이젠 훨씬 더 많은걸 학습해야해
	2. Not all bits are created equal - log-likelihood 는 high-level structure 보다는 low-level structure 에 반응해버린당
	3. Underlying structure 를 학습했더라도 이 structure 에 어떻게 접근하는지, 어떻게 이용할 수 있는지는 명확하지가 않다(representation learning)
* Generative Models
	* Modelling densities also gives us a generative model of the data
	* Density 를 학습하면, 생성도 가능하게 됨
	--> 생성을 해 보면 모델이 뭘 배웠는지를 알 수 있게 됨

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
	1. simple - 정의하기가 쉬움(순서만 정하면 됨)
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
* Autoregressive mixture models
	* 이전까지는 discrete 하게 해석했지만 continuous 하게 해석
	* 그 다음 step 이 등장할 xy coordinate 를 예측(그 다음으로 쓰여질 handwriting 이 어디로 향하게될지를 xy coordinate 로 예측하게 되는 것)



