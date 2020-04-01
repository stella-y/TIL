## svm
* 장 : 분류 기법중 최상으로 불림
* 단 : 직관적 해석이 불가능함

### 최대 마진 분류기(Maximal Margin Classifier)
* 훈련 관측치에서 주어진 초평면까지의 수직거리를 계산하고, 이 값에 따라 최적의 초평면 선택
* 이 최적의 초평면 선택의 기준이 분리 초평면에서 마진이 가장 큰 것
* 초 평면에 가장 가까운 분류 기점의 벡터 --> support vector

![svm](images/1_1.PNG "svm")

### support vector classifier
* 최대 마진 분류기의 확장
* soft margin 허용
* parameter 로 오류 허용의 정도를 결정함
	* soft cost 가 큰 값을 가지면 margin 의 폭은 작아지고, cost 가 작은값을 가지면 큰 마진을 가지게 됨

### support vector machine
* support vector classifier 가 비선형 커널과 결합 / 이때 얻어지는 분류기가 support vector machine
	* 커널 사용해서 변수공간 확장
	* 커널 차원을 높여서 다양한 결정경계 만든다.
* 주요 파라미터 두개(Cost / Gamma)
	* cost : svm 모델에 얼만큼 오차를 허용할 것인지를 나타냄
		* cost 값이 작으면 --> margin 폭 넓으짐
	* gamma : (hyperplane 이 아닌 kernel과 관련(radial 등)) 가우시안 함수의 표준편차를 조정
		* gamma 값 커지면 --> 작은 표준편차 가짐
* kernel
	* support vector classifier 는 suppert vector machine 의 1항과 같음
		* kernel 인자에 linear / cost 값으로 soft margin 설정
	* kernel 인자에 polynomial 입력, degree 로 차수 조절
	* kernel 인자에 radial 입력 - 방사형 커널 수행 / gamma 와 cost 조절


### svm 에서의 cost function

* Classification error
	* Margin line 을 더 그린다(wx+b=1 , wx+b=-1)
		* 이 거리를 같이 둔 상태로 error function 을 적용함
* Margin error
	* 마진을 error 로 만들고 싶은 것
		* --> (gradient descent 로 minimize 가능해짐)
	* Error function : large margin 에 대해서 적은 에러를 내고, small margin 에 대해서 많은 에러를 내는 함수를 찾아야 함
		* (되도록이면 큰 마진을 만들어내는게 안정적인 classification function 을 찾는것 이므로)
	* Margin = 2/|w|
	*  --> error=|w|^2(w는 vecrtor니까 --> w1^2+w2^2
	* --> 마진이 크면 에러는 작아지고, 마진이 작으면 에러는 작아진다

참고 : https://m.blog.naver.com/PostView.nhn?blogId=tjdudwo93&logNo=221051481147&proxyReferer=https%3A%2F%2Fwww.google.com%2F
