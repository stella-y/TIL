* activation function linearity 를 제거
1. sigmoid : x 값이 아주 크거나 작을 때에 기울기가 0이되어 그 역할이 없어져버림
2. relu :  computation 이 max —짱간단
	0이하에서는 죽어버려서 이걸 써서 돌리면 10~20% 는 못쓰게 돼 버리는 것
3. leaky relu - 죽지는 않아
4. parametric alpha - 이마저 학습하는 것

* optimization function
	1. sgd - gradient 가 0이 되는 구간에서 멈출 것(왔다갔다가 심해져)
	2. sgd+momentum - rho (관행적으로 0.1)
	3. nestrove momentum
		실수할 가능성을 줄이기 위해
		velocity 방향으로 진행한 후 그 지점에서 gradient 를 구해서 그만큼을 더 가게 돼
		nestrove momentum 계산 복잡해져서 꼼수써 —> 즉석에서 계산하기 보다는 그 전 step 의 gradient 에 velocity 값을 넣어서 구해
	4. adagrad - 무한대로 더해나가니깐 멈춰버릴 수가 있어
	5. rms prob - adagrad 에 decay rate 적용
	6. adam
		momentum + rms prob
		초기 값에 문제가 있을 거란ㄹ 데서 시작(초기 값이 분모가 너무 작아서 값이 뛰어버리는 일을 예방하기 위해 beta 사용
