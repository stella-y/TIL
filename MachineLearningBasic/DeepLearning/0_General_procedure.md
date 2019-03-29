## 딥러닝 네트워크 구성하는  일반적인 과정을 생각해보자아
1. 적절한 네트워크 선택
	* 구조(structure)
	* nonlinearity 획득 방법 : relu, tanh, ...
2. gradient 체크
	* 네트워크 구축은 잘 됐는데 그래디언트 계산이 혹시 잘못될 수도 있으니 체크
3. 학습 parameter 초기화
4. 학습 parameter 최적화
	* stochastic gradient vs adam
5. 과적합 방지
	* drop out, regularization, ...

참고 : https://ratsgo.github.io/deep%20learning/2017/04/22/NNtricks/