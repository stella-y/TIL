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

### Variational Auto-encoders
* We believe that there are underlying latent factors that affect the text/images/speech that we are observing --> 이게 이렇게 관찰된데는 다 이유가 있을거다 라는 가정 (해 봐야 알 수 있는 것들)
        * What is the content of the sentence?
        * Who is the writer/speaker?
	 What is their sentiment?
	What words are aligned to others in a translation?  (번역관점 - hard attention 관점)
	
### loss function
(그림)
* 위에 두개는 결국 같은 식(marginalized out)
* --> 평균 식이라고 볼 수 있으니깐 optimize 는 sampling 으로
* 복원 추출 샘플링개념처럼 이해할 수 있을 듯
* 근데 아무 근거 없이 샘플링하고 연결짓고 하는 과정을 계속 반복하다보니깐 엄청 비싸고 비효율적일 수 있음
* --> p(x|z)를 구할 때에 그냥 하지말고 p(z|x) 를 구해서 이어지도록 하자
* X --> p(z|x) --> z --> p(x|z) --> x 이 과정으로 평가하고 피드백 받을 수 ㄷ있도록

### reparametrization

