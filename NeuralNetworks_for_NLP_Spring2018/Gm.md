generative model
Autoencoders --> feature learning : pca 같은 걸로 dimension reduction 을 한 다음에 이 feature 를 다시 원복 해서 loss 를 계산해
Fully visible belief network
	이전 픽셀들로서 다음 픽셀을 예측함
	Previous pixel 의 정의해야함
	모델 자체는 뉴럴넷으로 
	Rnn 시도 (sequential 이니까) --> [pixel rnn --> 느려 (칸칸마다 softmax output 이 있고 이걸 softmax로 예측
	
Autoencoder 자체를 generation model 로 하기엔 뭔가 찝찝한 느낌 --> 이걸 smooth 한 그림으로 표현하는게 variational autoencoder 의 큰 그림


Intractable 하니까 이걸 approximate 해서 구하자

