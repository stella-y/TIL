## ensemble method
* Bagging
	* 여러 week learner 에게 subset 에 대해서 classification 을 의뢰
	* 이들의 결과를 voting 으로 겹쳐서 하나의 super model 을 만듦
* Boosting
	* 한쪽 분야에만 특화된 learner 들에게 자신에게 맞는 문제만 풀게 하고, 그 결과물을 합쳐서 super model 을 만듦
	* Adaboost
		* 첫번째 learner 에게 학습을 함 / 첫번째 learner 가 잘못 분류한 점들에 가중치를 부여해서 다음 learner 는 이를 잘 분류하게 함 이 과정을 반복하고, 이 model 들을 합쳐서 super model 을 만들어 냄
		![Adaboost](images/6_1.png "Adaboost")
		 Ln((7/8)/(1/8))=1.945910149055313 
		 Ln((4/8)/(4/8))=0 
		 Ln((2/8)/(6/8))=-1.09861228866811 
