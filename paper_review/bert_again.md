## bert
transformer model - attention is all youneed 에 최초로 등장
(attention 만 있으면 rnn, cnn 다 필요 없다 / nlp task 에서는)
### self attention
#### 타 방법론과의 비교
* rnn
	* 장점
		* 자연어 등 유동적 길이의 시퀀스 처리에 유리함
		* vanishing gradient 등의 문제를 gate 로 해결(lstm, grul 등)
	* 단점
		* 순차접근으로 병렬성이 부족
		* 게이트만으론 에러 전파문제 해결이 어려움
		* 필요없는 정보까지 전부 연산하여 낭비가 심함
		* 계층적 데이터는 처리가 어려움
* cnn
	* 장점
		* 단계마다 처리할 영역이 고정되어있어서 병렬화에 유리함
	* 단점(attention is all you need 에서 지적)
		* 시퀀스 양 끝의 정보를 합치려면 최소 log(n) 만큼의 depth 가 필요하게 됨
		* left-padding for text
* attention
	* seq to seq 에서 encoder 와 decoder 를 연결하는 핵심 이슈 중 하나
		* encoder 가 만든데에서 어디를 보는게 맞는가 등 
	* representation 단계에서부터 attention 을 사용한다면? --> self attention
		- 자기 자신에게서 어떤게 더 중요한지를 알아보는 layer 인 것
* self attention
	* intra attention 이라고도 부름 - 자기 자신에 대해서 다시 attention 을 줌
	* 한 시퀀스 내에서 요소가 다른 요소와 가지는 관계 정보와 연관성을 계산하는 것
	* 시퀀스 내의 모든 요소 사이의 pair 를 만들어서 attention 계산
	(연산 양이 많아보이지만 사실상 matrix 곱으로 바로 표현이 가능한 것)
	* 계산된 attention 값을 기준으로 가중 평균 줘서 해당 위치의 출력값을 계산함

* 왜 self attention
	* 계산 복잡도가 layer 당 o(1)
	* sequential operation 이 없어서 병렬화가 용이함
	* 모든 sequence 가 한 layer 에서 연결이 될 수 있음(cnn 은 log n 까지 쌓아야만 했지)

#### 방식
* three ways of attention
	* 1방향 attention
		- 하나의 입력이 얼마나의 영향을 미치냐를 표현하게 됨 (encoding 단계에서의 출력이 decoder 단계에서 얼마나 영향을 미치는가)
		- encoder -> decoder attention
	* 모든방향
		- 모든 요소 사이의 self attention
		- encoder 에서 이렇게 활용 가능하겠지
	* 이전의 출력값만 활용
		- decoder 에서의 attention
		- maskedDecoder self attention

### Transformer
* Transformer
	* masked attention - 이전 출력값만 사용하는 attention(나머지를 mask로 막아준다 라는 의미)
* seq to seq 모델의 병렬화
	* 학습시간 감소
* dot product attention
	* 기존의 attention 과 좀 달라
	* Query 와 key 를 곱했을 때에 유사도가 나올 수 있도록 학습시킨다
	--> 이렇게 해서 가중치가 나오면 그 가중치에다가 value 를 곱한다
	/키별로 쿼리랑 얼마나 유사한지 유사가중치를 곱해서 거기다 softmax를 곱하고 거기다가 value 를 곱하면 유사도 기준의 가중치를 구할 수 있을 것
	벡터 곱이 너무 커져버리면 값이 튈 수 있으니, 크기루트로 나눠주장
* scaled dot-product attention
	* additive attention
		* feed forward vector 를 태우다보니 dot product 보다는 성능이 훨씬 좋기는 해 --> 근데 병렬화에 불리해지지
	* dot product attention


* mask decoder 에서 자기 뒤에 있는걸 안쓰게



* self attention 의 단점
	* convolution 보다는 부분 만 갖고와서 뭔갈 하는게 어려워지기 때문에
* multi head attention
	* 128짜리 vector 를 16으로 쪼갠다면 8개가 생기는 것
	* 각각의 head 가 서로 다른 정보로 mapping해서 convolution 의 채널처럼 쓸 수있게 함
	* 서로 다른 정보들을 저장할 수 있게 하징

* point wise feed forward network
가중평균만 이제까지 줬으니 여기다가 feed forward vector 를 넣는다

* residual connection
	* 구현체마다 넣기도 혹은 안넣기도
	* 이전 값을 일정 비율 카피해서 더하는 과정임

* positional encoding
	* rnn 이나 cnn 은 position 정보가 자연스럽게 들어가지만 여기엔 없을 것 --> positional encoding 을 기존 vector 에 concat 해서 사용함
	* 이때에 sine, cosine graph 를 쓰는데, 매 위치마다 서로 다른 값을 주고 싶어서 저걸 넣는데, 사실 bert 에선 이거 필요없다고 말해... ㅋㅋㅋ



* bert
	* transformer model 이 잘 되니깐 이걸 일반적인 자연어모델에 사용할 수 있게 바꿔보자
	* 기존 e-d  model 과의 차이
		* 여러 문장 동시에 넣을 수 있게 함
		* positional encoding 대신에 position embedding 을 넣음
		* 세개를 transformer model 에 input 으로 그대로 넣는 것
	* 어떻게 학습?	
		1. masked value prediction
			* masking 처리를 해 놓고 이 부분이 뭔지 맞추는 것
			* 이 masking 처리 된 부분을 예측하게 되서, 보편적인 language model 이 생성될 수 있도록 하는 것
			* 10% masking, 10% random(강제 노이즈 생성), 80% 원본 
		2. 다음 문장 예측
			* 두개 문장을 주고, 이 두개 문장이 이어지는 문장인지, 이어지지 않는 문장인지를 맞추도록
			(결과들이 첫번째 attention 에 결과가 묶이도록 모델을 학습시키는 형태)
			* 여기에도 마스크를 씌운다고 나와있으나 그 비율에 대해서는 나와있지 않음
	* 이런식으로 학습시켜서 transfer learning 할 수 있게 둔 것





