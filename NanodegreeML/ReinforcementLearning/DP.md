# Dynamic programing
이미 환경에대해서 agent 가 다 알고 있다는 가정

* An iterative method
	* 모든 state 에서의 value를 0이라 가정
	* Current state에서의 value 값을 그 다음 state에서의 값을 이용하여 update(이건 아직까지 결정되어 있을 수없지 —> 첫번째 iteration 에서는 우리가 초기 세팅한대로 0이 들어가버릴거야)
	* 위에서 했던 iteration 을 반복해 (이번엔 다음 state 들이 다 0은 아니겠지) 
	* 이 과정을 반복하면 각 state 의 value가 true value 로 수렴할거야


* Iterative policy evaluation
	* Bellman update rule 이용
	* 모든 state  대해서 미리 알고 있는데 어려우니 state value를 지속적으로 update 해감
		* 처음엔 iteration 마다 변화가 크겠지만 어느 순간부터는 적어질 것
			* —> 충분히 작은 값 Theta 를 가정하여 이보다 변화가 작은 순간이 오면 iteration 을 중단하게 함
		* State value 값이 항상 어디론가 수렴한다는 게 증명돼있음…


* policy improvement --> policy iteration
	* 최소한 지금보다는 나은 policy 를 만들기 위해서 value function을 이용해 policy improvement 를 할 수 있음
		§ State value function 으로 action value function 생성
		§ Action value 가 가장 큰 방향으로 policy 설정

* Truncated policy iteration
	* --> variation
	* Policy evaluation step 을 차이가 작아졌을 때가 아니라 / 몇번 이상 update 한 후 멈추게 할 수 있음
	* 우리는 각 state에서 가장 큰 값을 찾으면 되는 것 뿐이라서 정말 완벽한 optimal value 를 찾을 때 까지 기다릴 필요가 없는 것!

* Policy improvement : given a value function corresponding to a policy, proposes a better policy
* Policy iteration : Finds the optima policy through successive rounds of evaluation and improvement
* (iterative)Policy Evaluation: Computes the value function corresponding to an arbitrary policy
* Value Iteration : Finds the optimal policy through successive rounds of evaluation and improvement



