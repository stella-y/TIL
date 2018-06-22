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
* GMF
```
MF를 NCF framework 의 special case 로 해석
User_vector 를 input layer 태워서 embedding vector 로 표현함  이걸 latent vector of user 로 이해할 수 있지
Layer1 을 element wise product 로 정의
Pie_1(p_u, q_i)=p_u@ q_i (@ denotes the element-wise product of vectors)
여기에다가 edge weight, activation function 적용
이논문에서는 sigmoid로, weight h를 log loss 로 적용함
Activation function 을 identity function, h 를 값이 1인 uniform vector 라고 가정하면 MF model 을 그대로 만들었다고 생각할 수 있음
H 를 uniform vector 가 아니라 뭔가 다른걸 넣게 되면 latent dimension 별로 중요도를 다르게 설정할 수도 있겠지
Activation function a_out 을 뭔가 non-linear 하게 쓴다면 linear mf model 보다 표현이 강화될 수 있겠지
여기서는 sigmoid function 을 activation function 으로, h를 앞에서의 log loss 로 학습
```
* MLP
```
Input 이 이렇게 두개의 pathway 로 존재할때 사실 얘를 그냥 concatenate 시켜서 하는건 아주 흔한 방법
근데 그냥 concatenation 하는건 user와 item 간의 관계를 전혀 반영하지 못함/  hidden layer 추가 (concatenate layer)
두 latent vector 간의 interaction 을 학습하기 위한 hidden layer 추가시킴
이렇게 하면 GMF 그냥 쓰는 것 보다(여기서는 only fixed element-wise product) flexibility, non-linearity 를 더 줄 수 있다!
Layer1에서 두개 concate 시키고
나머지 layer 에서 weight 곱하고 bias 더하고, activate
이때 실험적으로 해봤더니 relu
MLP – interaction function 을 learn 하기 위해서 non-linear kernel 쓰는 것
```
* NeuMF
```
GMF - Latent feature interaction 을 modeling 하기 위해 linear kernel 쓴 것
MLP – interaction function 을 learn 하기 위해서 non-linear kernel 쓰는 것
Neural tensor network concept 하나의 레이어에 쑤셔 넣는 것optimal embedding size 가 두 network 가 아주 달라
그냥 same embedding 을 사용하게 하는건 성능향상에 기여하지 못함
Neural tensor network concept 은 사용하지 못하게 된다
```
```
Embedding 도 서로 따로 하고, 마지막 hidden layer 에서 concatenate 하는 방식
Pretraining
NeuMF : non-convex
  ㄴ ensemble of GMF & MLP 모델 --> 각각의 pretrained model 활용
두 모델이 converge 할 때까지 training 시키고(start with random initializations), 이때의 model parameter 를 NeuMF 의 model parameter 로 이용함
두 모델의 앙상블 이니깐 각각의 pretrained model 을 NeuMF layer 에서 사용함
Random 하게 initialize 해서 converge 할때까지 따로
그러고 나서 weight 를 concatenate
각각 training 시킬때는 
Learning rate tuning 이 필요 없고 converge 속도가 빨라서 adam
```
