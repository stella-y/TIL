### 텍스트 분류 벤치마크 
* AG’s news articles
* Sogou news corpora
* Amazon Review Full
* Amazon Review Polarity
* DBPedia
* Yahoo Answers
* Yelp Review Full
* Yelp Review Polarity

Kaggle에서 성공한 솔루션을 살펴보면, 고도로 맞춤화된 복잡한 ensemble이 지배적

* 신경망 기반 텍스트 분류기
	* Embedding
	* Deep representation
	* Fully connected part
* Dense Classifier
	* 완벽하게 연결된 부분은 deep representation에 대한 일련의 변환을 수행하고 마지막으로 각 클래스의 점수를 출력 
	* fully connected layer
	* regularization
	* (선택 사항) (hyperbolic tangent 또는 ELU)
Dropout
