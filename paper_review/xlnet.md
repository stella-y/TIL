## Transformer XL
* xl net 의 기반
* language model 에 특화됨 - lm(그 다음 단어 예측)
* long context 다루는 부분이 contribution
* gpu 에 들어갈 수 있는 양에 한계가 있어서 256, 512 단어 등으로 잘라서 넣게 될 것
* rnn 에서는 긴걸 학습시킬 방법이 있었음 --> bptt 
	* 앞의 block 에서 학습한 것 자체를 그 다음 block 으로 넘기는 방법으로 학습한 정보를 유지할 수 있음
	* transformer 는 이게 안됨(block 단위간 학습 결과 전달이 불가능 함 --> 이걸 address 하는게 이 논문의 가장 큰 contribution)
* long term dependency 를 학습시키고 싶다는게 목적인 것
* 제안
	1. segment-level recurrence
	2. relative positional embeddings
* 앞에꺼는 값 참조만 하고, backpropagation 으로 값 update 를 하지는 않는 것
sg(stop gradient)
o : concatenate
w : weight matrix
stop gradient 를 concat 하는 과정이 붙었다는 정도가 그냥 transformer 와의 차이점
previous segment 는 memory 가 허용하는 범위내에서 다 넣게 하면 됨

position embedding - block 마다 고정된 값으로(sin 곡선)
block 각각에서 동일한 sin 곡선으로 position embedding 을 하게 되면, 이게 어떤 block 에서 왔는지를 표현할 수 없게 됨

쿼리위치에서의 상대 위치만 알면 되지 않을까(절대 위치를 꼭 알아야하는가?) 라는 아이디어 --> relative position 사용

현재 자기 위치 기준으로 sin 곡선에 대응시키는 방식으로 embedding 하는 것
+ U_i transpose 같은 경우엔 trainable parameter 첨가해서 학습 가능하게 바꿈

근데 여기서는 downstream task 에 대한 내용이 빠졌고, document generation 내용이 없어서 위 논문은 리젝먹었었음
------------------------------------------------

## xlnet
* autoregressive(전통적(rnn 등)) / autoencoding(bert)
	* autoregressive
		* 앞의 결과로 뒤의 결과를 예측하는 것
		* forward 기준의 context 밖에 알 수 없기 때문에, backward 도 한번 해서, concat 하는 방식으로 사용한 것
	* autoencoding
		* denoising autoencoder 방식이라 생각할 수 있음
		* 특정 지점을 corruption 한 후에 주변의 정보로 복구하는 형태의 디자인이라 해석할 수도 있을 것
* bert's limitation
	* (M, M, is, a, city)
	* 위의 글을 예측할때에 T_bert=log()
	long term dependency 해결

* permutation language model
	* permutation 한 이후에, 다음껄 예측하는 방식으로 가도록 함
	* 모든 permutation 을 취한 후, 등장할 확률에 기대값을 취하면 될것이라 기대하는 것
* 근데 모든 permutation 을 취하는건 연산량이 너무 많을 것/ permutation 을 취하는 space 를 줄였다.

permutation 을 하면 위치 정보가 빠지게 될 것 --> given 에 위치 정보를 함께 넣게 됨(이게 content stream)
down stream task 에서는 transformer model 은 원래 자기 자신을 봐야하는데, language model 에서는 이걸 쓰는게 cheating 일 것 --> 그래서 down stream task 에서는 query stream 을 빼고, content stream 만 쓰게 됨
language model 에서는 

위치 정보를 드러낼 뭔가의 z_t 함수
position embedding 자체에, weight matrix 와 함께 학습시켜서, PE * WE 가 position 을 나타낼 뭔가가 될 수 있도록 만드는 것

squad contest 에서 single model 에서는 1등




















