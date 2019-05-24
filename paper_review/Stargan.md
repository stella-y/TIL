## Stargan : Unified Generative Adversarial Networks for multi-domain Image-to-Image translation

### 문제 정의
* image to image translation : e.g. 실사 to 스케치, 스케치 to 실사 등
	* 제일 쉽게는 paired image set 일 것
	* 근데 pair 되지 않은 data 에 대해서도 할 수 있게 한 알고리즘이 개발됨(cycle gan)
* multi domain image to image translation
	* 하나의 이미지로부터 여러개의 이미지형태를 뽑아내는 것
	* e.g. 실사 to 고흐풍, 피카소풍 등등등...
* cycle gan
	* gan : generator, descriminator 가 있고, 이 두 조건으로 generator 가 conceptualy 유사한 뭔가를 만들어낼 수 있게 하는 컨셉
	* cycle gan : generator 가 고흐 to 피카소면, 그 반대로 피카소 to 고흐 인 F 를 만들어둠
		* X -G-> Y -F-> X^ 일때 X=X^ 이길 기대하는 것
		* 이렇게 하면 paired data 의 제약이 없을 수 있게 됨(x와 y 를 직접 비교할 필요가 필요 없게 됨)
		* 심지어 성능도 괜찮았음
		* idea 가 워낙 좋아서 다른 도메인에도 많이 쓰임 (nlp / translation 등)
	* loss function
		* adversarial loss : descriminator 로 비교(기존 gan 의 loss)
		* cycle-consistency loss (픽셀 단위의 차이를 봄)
* Star Gan
	* cycle gan 을 multi domain 으로 해내려면, 모든 pair 에 대해서 generator 를 만들 필요가 생김
	* 이걸 다른 방식으로 만드는게 star gan --> generator 를 하나만 쓰겠다!
	* descriminator 관점 : domain classification 을 하는 descriminator 를 같이 넣음(real fake 구분과 domain 을 구분을 동시에 함)
	* generator 관점 : input 에 target domain 을 갖이 넣게 됨, 그리고 나서 다시 cycle gan 에서처럼 loss 값 비교
	* objective & loss
		* descriminator 를 학습할때엔 
		* rule of thumbs -  lambda_cls =1, lamda_rec=10

### 방법
* traininng with multiple datasets
	* label 에 대해서 어떻게 학습시킬 것인가 --> concat 시켜버림
	* masking 효과를 주기 위해 masking vector 를 넣어 둠
	* discriminator 는 known label 에 대해서만 학습하게 했다고 함(generate 한거에까지 적용하진 않음)
* implementation wgan
	* loss function 에서 log 를 제거했다고 함
	* gradient 가 1이랑 가까워야 한다는 제약을 하나 더 넣은 것

### limitation
* 학습시킬때에 이미지 크기를 잘 맞춰야 학습이 잘 되더라
* claimed multiple datasets but provide the results on two datasets



### challenge











