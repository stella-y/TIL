## Gradient / Backpropagation / Activation function
### gradient
* 편미분 값들의 벡터
![gradient](images/b1_1.png "gradient")
![gradient](images/b1_2.png "gradient")
![gradient](images/b1_3.png "gradient")

### backpropagation
* forward step - gate 통과하면서 실제 값을 계산
* backward step - gate 를 반대로 통과하면서 chain rule 로 각 gate 에서의 gradient 값을 계산
	* 전후 step 의 output 값과 gradient 값을 이용해서 현재 노드에서의 gradient 값을 계산해나감
* 보다 큰(혹은 작은) 최종 출력 값을 얻도록 게이트들이 자신들의 출력이 (얼마나 강하게) 증가하길 원하는지 또는 감소하길 원하는지 서로 소통하는 것으로 간주할 수 있다.

### Activation function
* 입력 신호의 총 합을 출력신호로 변환하는 함수
* perceptron 과 neural net 의 차이점
* 이거 없이 그냥 쌓으면 hidden layer 가 있다는 의미가 사라질 수가 있음
(h(x)=cx 를 활성화함수로 사용한 3층 네트워크 <==> y(x)=h(h(h(x)))
실은 y(x)=ax와 똑같은 식 인거라 a=c3이라고만 하면 끝)




http://aikorea.org/cs231n/optimization-2/
https://ratsgo.github.io/deep%20learning/2017/04/22/NNtricks/