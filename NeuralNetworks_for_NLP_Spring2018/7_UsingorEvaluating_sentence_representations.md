## sentence representation
* 문장을 vector 로
	![sent_vec](images/7_5.png "sent_vec")
	1. 문장 전체를 1차원 벡터(3\*1)로 만들거나
	2. 아니면 단어 하나씩에대해서 vector 하나로 놓고, 그 네개 단어를 붙여서 다차원 벡터를 만들거나(3\*4) --> attention 계열이 이쪽을 활용한 것
* 활용
	* IR(검색) 쪽에서는 특히...
	* sentence classification / paraphrase identification / semantic similarity / entailment / retrieval

### Sentence Classification
* topic, sentiment, subjectivity/objectivity 등등 여러가지로 분류해둬
	![general_model](images/7_6.png "general_model")
	embedding 붙여서 cnn or rnn 후 softmax --> prob 계산

#### Paraphrase Identification
* A 문장과 B 문장이 주어졌을 때에 이 두 문장의 의미가 같은지 다른지를 예측
	* '완전히 같다'의 정확한 정의에 대해서는 의견이 분분함
* 데이터 예시
	* Microsoft Research Paraphrase Corpus (Dolan and Brockett 2005) 
		* news corpus 를 다 모은다음에 비슷해 보이는걸 분리함
		--> 5800 sentences (질은 좋은데 양이 적엉)
* 모델1 - sentence 를 vector 로 나타내고 이 둘사이의 similarity 를 계산(두 문장이 같다 틀리다)하는 classifier(logistic regression or NN or jaccard 등 여러가지)로 돌려
	![PI](images/7_2.png "PI")
	1. Skip-thought Vectors (Kiros et al. 2015)
		* word to vec 의 sentence 버전
			* google 논문
			* general method
		* unsupervised training : large scale data로 주변 문장들 학습 (Using encoder-decoder)
		  --> 주변에 나왔으면 비슷한 문장일것이다 라는 가정으로
		![Skip-thought](images/7_1.png "Skip-thought")
			그림에서
				좌측의 문장과 거기서 나온 sentence vector
				좌측의 문장을 돌렸을 때에 이전문장(그림의 우측 상단)과 이후문장(그림의 우측 하단)을 잘 예측할 수 있는 모델로 구성
		* full text 형태의 task 에 잘 working 할 것 (domain 에 따라 working 할수도, 하지 않을수도)
* 모델2 - multiple-vector representation(단어 하나하나마다 vector 1차원으로 해서 문장 하나는 다차원 vector) 을 계산해서 1번과 비슷한 결정을 함
	![PI2](images/7_3.png "PI2")
	1.  Convolutional Features + Matrix-based Pooling (Yin and Schutze 2015)
		![PI2_e](images/7_4.png "PI2_e")
		1. convolution 해가면서 압축
		2. 위에서 두번째 벡터는 1번문장에서 온 벡터 + 두 문장의 상호관계에서 온 두개의 벡터 + 2번 문장에서 온 벡터
		3. 맨 위에서는 이 벡터들 합쳐서 logistic regression
	2. Paraphrase Detection w/ Discriminative Embeddings (Ji and Eisenstein 2013)
		* word/context vector 에 대해 matrix factorization
		(딥러닝 보다, mf 같은 방법론이 여전히 유효하다! 라는 의미에서 --> 의외로 paraphrasing 에서는 지금도 mf 방법론의 성능이 제일 좋대- 위에서 나왔던 MSRPC 데이터에대해 적용해보면 이게 제일 좋대)
		* word vs context 의 matrix 가 있을 때에 이걸 mf 하고나면 context를 모르던 word 들에 대해서도 채워질 것
		* 이를 다시 kl-divergence 로
		![using_mf](images/7_7.png "using_mf")
		우측 상위로 갈수록 비슷한 단어 / 좌측 하단으로 갈 수록 안비슷한 단어

## Semantic Similarity
* 의미적인 유사도
* 데이터셋 예시
	* SICK dataset
		* flickr/video description sentence 이용
		* 전처리
			* normalize - 동의어로 replace
			* create opposit - negation, antonyms(반의어) 등 삽입
			* scramble words - 단어 순서 섞기(?)
		* 이러고 나서 사람들에게 물어서 이 문장이 얼마나 유사한지를 물어봄
		* evaluation procedure
			* (아까는 classification 문제로 봤지만)이번엔 regression 문제로 봐서, score 가 사람이 매긴것과 얼마나 비슷한지를 평가
* Siamese LSTM Architecture
	![Siamese](images/7_8.png "Siamese")
	* 과정
		* 두 문장에 대해서 곱해지는 weight matrix 를 완전히 같게 해
		* 두 문장의 vector 를 알아내고
		* similarity 는 l1 loss 를 쓴 것
		* sigmoid 해서 scale 이 0에서 1사이로 나오게 해서
	* 단순한 모델인데도 성능은 짱 좋대

## Textual Entailment
* 의미
	* Entailment: if A is true, then B is true (c.f. paraphrase, where opposite is also true)
		* The woman bought a sandwich for lunch
		→ The woman bought lunch
		숨은 의미로 참임을 알 수 있음
	* Contradiction : A 가 참이면 B 가 거짓임을 알 수 있음
	* Neutral : 관계가 없어서 서로의 참 거짓 여부를 알 수 없는 것
* 데이터 셋 :Stanford Natural Language Inference Dataset
	* Flickr caption 만들어(Entailment, Neutral, Contradiction 생성)
* Multi-perspective Matching for NLI (Wang et al. 2017)
	![Entail1](images/7_9.png "Entail1")
	* 관계를 알아내야 하는 두개의 문장(맨아래 두개)이 들어와
	* Context representation layer 에서는 sequence 니깐 그냥 BiRNN 써버려
	* Matching layer 에서는 matrix 전체가 들어오게 되니깐 attention 을 써 (이 큰 매트릭스 안에서 어떤 정보에 집중해야하는지 알아내야 하니깐)
	* 그러고 나면 Matching layer 위의 파란색 vector 에는 Context 정보 + attention 정보를 합친게 만들어질거야
	* BiRNN 을 다시 돌려
	* Sequence 를 다 돌린 마지막 정보를 aggregation layer 로 올려서 concat 시켜
	* 그러고 regression 해서 softmax 빡
* Interesting Result: Entailment → Generalize (Conneau et al. 2017)
	* entailment 는 text 의 뉘앙스, 컨텍스트 등을 잘 파악함 --> unsupervised model(skip thought -> 뉘앙스 없이 앞뒤 문장정도, language model 등) 좀 더 generalize 한 enbedding 결과를 제공해 줄 수 있을거라는 생각
	* 논문 결과로는 이게 꽤 괜찮은 결과였댕
	* 근데 한글은 없어용

## Retrieval
* Retrieval idea
	* input sequence 가 주어지면 거기에 맞는 무언가를 찾아주는 것(검색) - 결과는 text 일수도, image 일수도
* Basie Idea
	* 모든 원본 텍스트 같은걸 vector 화 / indexing
	* query 왔을 떄에 similarity 를 구하건 뭘 하건 해서 답변을 내게 하면 될 것
* First attempt
	* 검색 task 에 대해서는 학습이 아니고, 고정된 function 으로 vector 화 해왔어(TF-IDF, BM25 등)
	* 이걸 이젠 학습 가능한 function 으로 바꿔보자
		* lossfunction 지정(답에 가까울 수록 작아지게)
* Margin-based Training
	* loss function=max(0, 1+x_n-x_p)
	





