## Machine learning
- 주어진 데이터를 가장 잘 설명하는 '함수'를 찾는 알고리즘을 디자인
- 확률 관점에서 : probability density 를 찾는 과정
	- 함수 대신 확률 분포를 가정하고, 적절한 확률 분포의 parameter 를 추론하는 과정
* 전자는 function parameter 찾기 / 후자는 probability density function parameter 찾기

## PDF(probability density function)
* 특정 구간에 속할 확률를 구하기 위한 함수
(e.g. 1부터 6사이의 (무한히 많은)숫자가 있을때 4에서 5사이의 숫자가 뽑힐 확률)
* 연속 사건의 경우 특정 사건이 일어날 확률은 모두 0 이며 어떤 구간에 속할 확률은 PDF 를 통해 구할 수 있음

## likelihood
* 직관적 정의 : 확률 분포 함수의 y값
	* 셀수 있는 사건 : 가능도=확률
	* 연속 사건 : 가능도 != 확률, 가능도 = PDF 값

## MLE(Maximum Likelihood Estimator / 최대 가능도 추정량)
* 기초적인 통계 분석에서 회귀 분석에 이르기까지 거의 모든 통계 분석에서 참값을 추정하는 원리
* 관측할 결과가 나올 가능성을 최대로 하는 실제의 값은 얼마일지를 추정
* random variable parameter 를 추정하는 방법 중 하나
* density function(f), parameter(theta), observation(x)
	* f(.|theta) 여기서 observation x만 알게되면 f(x|theta)를 알게될 것
	* f 가 가우시안이라면 θ는 mean μ와 covariance Σ일 것이고, Bernoulli라면 0≤p≤1
* likelihood를 최대로 만드는 값을 선택하는 것
(즉 theta 가 주어지고, 그 theta 에 대한 데이터들의 확률을 최대화)
	* 선택한 값 theta_hat
	θ^=argmaxθL(θ;X)=argmaxθf(X|θ)
	* i.i.d(independent and identical distributed)이면 f(X|θ)=∏if(xi|θ) 가 되며, 여기에 log를 씌우면 덧셈 꼴 --> 보통은 loglikelihood 로 parameter estimation 계산
		* log는 단조증가함수 -->  log를 취했을 때 최대값을 가지는 지점과 원래 최대값을 가지는 지점이 동일
		* 보통 곱셈보다 덧셈이 계산이 더 간편하므로
* 관찰 값에 너무 민감한건 단점
	* 동전 10번 던져서 앞면 10번 나오면 앞면이 나올 확률은 1이라 계산하는 것
- e.g. 키를 5번 측정했을 때 178,179,180,181,182cm이 나올 가능성이 최대가 되는 나의 키는 얼마일까?
	1. 키의 참값이 μ일 때 측정값은 평균 μ, 분산 σ2인 정규분포를 따른다.
	2. 키의 측정값이 x일 때의 가능도, 즉 정규분포의 y값은 12π√σe−(x−μ)22σ2이다.
	3. 5번 측정한 키가 178,179,180,181,182가 나올 가능도 L은 각각의 가능도의 곱인 12π√σ2e−(178−μ)22σ2×12π√σ2e−(179−μ)22σ2×12π√σ2e−(180−μ)22σ2×12π√σ2e−(181−μ)22σ2×12π√σ2e−(182−μ)22σ2이다.
	4. L이 최대가 된다는 것은 e−(178−μ)22σ2×e−(179−μ)22σ2×e−(180−μ)22σ2×e−(181−μ)22σ2×e−(182−μ)22σ2 = e−((178−μ)2+(179−μ)2+(180−μ)2+(181−μ)2+(182−μ)22σ2)가 최대가 된다는 뜻이고, 이는 다시 (178−μ)2+(179−μ)2+(180−μ)2+(181−μ)2+(182−μ)2가 최소가 되는 것으로 해석할 수 있다.
	5. (178−μ)2+(179−μ)2+(180−μ)2+(181−μ)2+(182−μ)2은 μ=180에서 최소값을 가짐을 쉽게 알 수 있고, 따라서 μ의 MLE는 180이다.

## MAP
* 주어진 데이터에 대해 최대 확률을 갖는 theta 를 찾는 것
* θ^=argmaxθf(θ|X)
* 여러 parameter 에서 데이터가 주어졌을 때 가장 확률이 높은 theta 를 구하는 것
θ^=argmaxθf(θ|X)=argmaxθf(X|θ)f(θ)/f(X)=argmaxθL(θ;X)f(θ)/f(X)
(by bayes' theorem)
==> θ^=argmaxθL(θ;X)f(θ) 
(f(x) 는 θ에 영향받지 않으므로)



참고 : http://rstudio-pubs-static.s3.amazonaws.com/204928_c2d6c62565b74a4987e935f756badfba.html