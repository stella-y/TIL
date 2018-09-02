## VAE
* Generative model 중 하나
* Latent random variable 을 써서 모델링을 한다 --> 이렇게 쓰는 방법중 하나에 vae 가 있는 것
* Latent variable 하나하나에 의미가 있을거라는 가정

### preliminaries
* Discriminative model : p(y|x)를 바로 만드는 것
	* 분류 문제라면 분류하는 선을 학습하는 것)
* Generative model :  p(x,y)를 학습하는 것
	* 분류 문제라도 각 class 의 분포 자체를 학습해 --> p(x)를 만들 수 있어
	* 왜냐하면 분포를 학습했으니깐 그 안에서 당연히 sampling or generate 할 수 있겠지
* ex
	* Standard BiLSTM POS tagger
	* Globally normalized CRF POS tagger 
	* Language mode

* variable 종류
	* 관찰된 변수 vs 관찰되지 않은 변수(Observed / latent)
		* Latent 이런게 있을거라고 가정해놓고, observed 로부터 추론해서 사용 / 온도를 보고 실내인지 실외인지 추정하는 것도
	* Deterministic vs random(stochastic)
		* Y=5X+4 인데 X ~(0,1) 이런거
		* ex
			* The input word ids f - o / d
			* The encoder hidden states h - i/d
			* The attention values a 
			* The output word ids e

