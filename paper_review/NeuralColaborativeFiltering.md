* intro
	* Matrix factorization
		Cf 를 할때에 필요
		User 와 item 을 더 낮은 차원의 latent vector 로 나타내고, user 랑 item 간의 interaction 을 이 latent vector 의 inner product 가 될 수 있도록
	* Latent space
		Inner product 방식으로 factorization 을 진행하면 vector 의 차원에 따라서 왜곡이 생길 수 있다  너무 작은 차원으로 하다보면 왜곡이 생길 수 밖에 없다
	* 이런걸 예방하려면 factorizing 하는 vector 의 크기를 너무 줄이면 안되는데, 이렇게 하면 generalization 에 문제가 생길 수 있다(overfitting 같은?)
	* Inner product 로의 factorization 대신 Interaction function 을 data 로부터 learning 시키자

* related work
	* User 랑 item 의 interaction 을 표현할때에는 아직까지도 inner product 에 의존하는 경향이 크다.
* method
	* ncf framework

``` 
Neural Collaborative filtering framework
NCF adopts two pathways to model users and items. 

Input layer :
	User 에 대한 latent vector / item 에 대한 latent vector
	One hot encoding

	이 벡터 안에 뭘 넣어도 상관 없음-categorical data 든 뭐든 다 때려넣어서 만들 수 있음
	(논문에는 pure 하게 하기 위해서(다른 방식과의 비교 등?) user, item 의 identity 로만 했다고 되어있음)

Embedding layer : fully connected layer / sparse representation 을 dense 하게

Last layer X : dimension of it – capability of model  여기서 최종 score y_ui [0, 1] 내 놓음
	target value y와의 pointwise loss 를 minimize 시키는 방식으로 training
(observed interaction – unobserved interactions 은 negative instance 로 간주한다)

Binary cross entropy function

Likelihood function구하고 여기에 negative logarithm  구하고  이게 ncf의 objective function(이게 binary cross-entropy function 즉 log loss 와 같지)  사실 이걸 recommendation 에서는 loss function 으로 잘 안쓰기는 하는데 4.3 장에서 이게 효율이 좋다는걸 practical 하게 보임
	log loss 를 최소화 시키는 방향으로! SGD 이용

Negative instance – unobserved interaction 중에서 uniformly sample 함 – observed interaction 수에 비례하게!
Cold start 를 막기 위해서 이 논문에서는 user, item 을 표현한 content feature 들을 썼다!(further improvement 로 item popularity bias를 넣어서 sampling 을 할 수도 있을 것 같다)



이걸 sgd 로 최소화 시키는 지점 찾음

Loss 를 그냥 구한건 아니고 weight*(y_ui-yhat_ui)^2 y_ui 가. Binarized 1 or 0

```

