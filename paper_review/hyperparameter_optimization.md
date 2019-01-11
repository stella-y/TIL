## practical bayesian optimization of machine learning algorithm
* https://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf
* https://www.youtube.com/watch?v=MnHCe8tGjQ8&feature=youtu.be
* hyper parameter tuning 에 대한 연구 --> bayesian optimization 을 이용해서 이를 하겠다는 것
* motivation
	* 여러 hyper parameter issue - 감으로 혹은 다양히 실험 한 후에 적용하는 경우가 많음
		* 재생산성 문제... 이것때문에 논문 재현이 안되기도 한다
	* black magic... 
	* 일반적으로 이전에 활용했던 방법들
		grid search : 범위를 설정해서 grid 찍어 이때의 성능을 각각 비교, random search : random 하게 값 찍어다가 실험 반복 후 성능 비교
* bayesian optimization
	* objective 위한 확률모델 만들고
	* compute the posterior predictive distribution
	* exploit and exploration 반복

```
본래의 문제는 function 이 주어졌을 때에 이를 minimize 하는 hyper parameter x 를 찾는게 목표인 것
--> 이를 그냥 풀 수는 없으니깐
대신 acquisition function 을 정의하게 됨 /. -> 이 지점에서 loss 가 클거다 낮을거다를 예측할 수 있게 해주는 function 을 정의 이 function 에 대한 optimization 을 정의함
```
* gaussian process - 점을 하나씩 더 찍을때마다 one sigma 공간이 줄어들게 됨 --> 모델의 정확성이 올라가는 것
* prior measure - 다음 loss 의 기댓값 (이정도로 줄어들 수 있을 것 같아)
* posterior measure
* acquisition function 정의 
	* 진짜 loss function 을 사용하면 너무 무거움
	* -> 이걸 대신(모사)할 수 있는 acquisition function 제시
	* 어떤 걸 하는게 우리한테 이득이 클지에 대해서 나타내주는 function을 새로이 정의하는 것
	* 지금 알고있는 곳 보다 높은 값을 얻게 될 가능성이 높은 지점에서 acquisition function 의 값이 크게 나올 것 --> expected improvement 값을 쓰게 되는 것
* 이런 acquisition function 의 값을 exploit 하거나, noise 를 더 줘서 explore 하는 과정으로 최선의 값을 얻을 수 있는 hyper parameter 를 찾아가는 과정이다 (다음번에 어디를 관찰하는게 가장 좋은 선택인지를 acquisition function 을 이용하는 것)
* optimization - gaussian process


*** 사실 이위의 내용들은 이미 다른 논문들에서 이미 정의한 바가 있는 것이고, 이를 어떻게 practical 하게 만드는지가 이 논문의 contribution 인 것 ***

* propose 1 : choice of covariance function & choice hyperparameters
	* covariance function 으로 martern 5/2 kernel 을 쓰는걸 제안
	* hyper parameter 를 날려버리고(평균의 형태를 만들고), 여기에 mcmc 를 쓰게 되면 loss 가 빠르게 줄어들더라
* propose 2 : modeling costs
	* 이전까지는 시간 같은 cost 를 model 에 넣지는 않았을 것
	* expected improvement per second
	* --> 빠르게 진행이 가능해지더라!
* propose 3: monte carlo acquisition for parallelizing
	* proposed : fantasize the outcome of pending candidate


응용
* hyperopt - gaussian process 로 진행하지는 않고, tree 구조로 만들고 나서 route 를 찾는 tp 라는 알고리즘을 쓰게 됨
	* 짧게 걸리는 프로젝트에서는 활용이 용이하다(gaussian process 를 쓰지 않는다는 점의 trade off)
	* 
* bayesianOpt
	* 실제 위 논문을 구현한건 이아이 : https://github.com/fmfn/BayesianOptimization











