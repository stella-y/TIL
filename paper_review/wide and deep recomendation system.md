## Wide & Deep Learning for Recommender Systems
(google, 2016)
### insight
- 추천 문제에서의 성능 향상 위한 관점을 memorization, generalization 으로 정의하고, 이 두가지 관점 모두에서 좋은 성능을 보일만한 알고리즘을 개발함
- feature 활용 방식, 전체 시스템 아키텍쳐, 문제 해결의 관점과 이를 기반으로 분석한 선행연구 정리에 있어서는 참고할만함

### 개념정의
- Memorization
	- 각각의 특징을 기억
	- 이전 데이터로부터, 이것과 이것은 연관(동시 발생하는 경향이 있다)이 있다 라는걸 알아냄 (Frequent co-occurrence of items or features)
	- 단점 : 
		- 이미 있던 데이터를 기반해서만 추론이 가능함
		- 기억하는 값들만 잘 찾음 → overfitting
- Generalization
	- 특징을 일반화
	- 연관도의 전이성을 바탕으로 이전에는 드물게 발생했던 새로운 feature 조합을 찾아냄(diversity of recommendation)
	- 단점 : 특징들이 추상화되면서 underfitting 될 수 있음

### Memorization, Generalization 선행 연구
#### 일반적 industrial setting
- Logistic regression with binarized sparse features with one-hot encoding
- **Memorization**
	- sparse feature 에 대한 cross-product transformation
		- crossed feature : frequent co-occurence of items
		- Feature 간 동시발생 여부가 feature 인 것
		- 수작업으로 feature engineering 해야함
- **Generalization**
	- feature 자체를 category 화 → 수작업...

#### Embedding-based model
- FM(Factorization Machine), dnn
- Underlying query-item matrix 가 너무 sparse 하거나, high-rank 몇개가 고정된 경우 embedding 이 효율적으로 생성되기 어려울 수 있음
	- → over generalized 될 위험이 있음(under fitting)

#### Factorization machines with libFM (2012)
- wide linear model(with cross-product feature) + deep neural net
- deep network 로 생성한 low dimensional embedding layer 를 만들고, 두 벡터의 dot product 를 factorizing 함

### Feature 활용
- Score 는 P(y|X)
- Feature(query)
	- User feature
		- e.g. country, language
	- Contextual feature
		- e.g. device, hour of the day, day of the week
	- Impression feature
		- e.g. app age, historical statistics of an app

### Recomender system architecture
![recommender_system](images/wideanddeep1.png "recommender system")
#### Retrieval system
- 후보군을 줄이는 역할
- score 를 계산하는건 여기서 걸러진 item(전체 item 에 대해서 추천 score 를 계산하지 않음)

#### Model
![model](images/wideanddeep2.png "model")
- The wide component
	- Generalized linear model (y=w^T \*x +b)
	- cross-product transformation 사용
- The deep component
	- embedding layer + hidden layer
- joint training
	- Ensemble 은 모델들을 각각 트레이닝 한 후에, 예측할때 결과를 합치는 방식이라면, joint training 은 각 파라미터들을 동시에 학습함

### System implementation
![System](images/wideanddeep3.png "System")
- Data Generation
	- Vocabulary Generator : categorical feature string 을 정수 id 로 변환
- Model Training
	- 트레이닝 시간 줄이기 위해서 이전 모델에서의 embedding과 linear model weight 를 그대로 사용



