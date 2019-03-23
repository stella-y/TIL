### gradient 의 간단한 표현과 이해
* gradient : 편미분 값들의 벡터
	![gradient](images/b1_1.png "gradient")
	![gradient](images/b1_2.png "gradient")
	![gradient](images/b1_3.png "gradient")
* backpropagation :
	* forward step - gate 통과하면서 실제 값을 계산
	* backward step - gate 를 반대로 통과하면서 chain rule 로 각 gate 에서의 gradient 값을 계산
	* 보다 큰(혹은 작은) 최종 출력 값을 얻도록 게이트들이 자신들의 출력이 (얼마나 강하게) 증가하길 원하는지 또는 감소하길 원하는지 서로 소통하는 것으로 간주할 수 있다.


http://aikorea.org/cs231n/optimization-2/