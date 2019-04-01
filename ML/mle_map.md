## MLE
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
		* 보통 곱셈보다 덧셈이 계산이 더 간편하
* 관찰 값에 너무 민감한건 단점

## MAP
* 주어진 데이터에 대해 최대 확률을 갖는 theta 를 찾는 것
* θ^=argmaxθf(θ|X)
* 여러 parameter 에서 데이터가 주어졌을 때 가장 확률이 높은 theta 를 구하는 것
θ^=argmaxθf(θ|X)=argmaxθf(X|θ)f(θ)f(X)=argmaxθL(θ;X)f(θ)f(X)
(by bayes' theorem)


참고 : http://rstudio-pubs-static.s3.amazonaws.com/204928_c2d6c62565b74a4987e935f756badfba.html