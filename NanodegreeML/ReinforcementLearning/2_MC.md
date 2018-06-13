# MC(Monte Carlo) Prediction
-- monte carlo 방식으로 state value function, action function 구하기

* 기본 과정 : Env(state, reward) --> agent(action) --> env -> agent ->…
* The prediction problem
	* Given a policy pie, determine V_pie(or Q_pie)
	* (from interaction with the environment)
* Off policy method
	* 여러 개의 episode
	* 이 episode 들을 estimating value function 에 사용
		* 각 episode, 각 state 에서 얻게 되는 reward 의 값을 평균내서 그 state 의 value function 으로 이용
		* 여러 번 방문할 경우 first visit 만 계산 --> first visit MC method
		* 전부 다 계산 --> every-visit MC method

* (MC로 하는 이유 —> 모든 상황에 대한 정보가 항상 있는건 이니니까 / env 와의 상호작용으로 얻을 수 있는 정보들만으로 구성해야 하니깐
* Next step in Dynamic programming setting
	* = getting action function 
		* convert V_pie to Q_pie
		* 근데 이걸 쓸 수가 없지
	* action value 구할 때에도 mc method 이용
	* 단 이때에는 state와 action 을 동시해 고려해서 reward의 평균을 내야겠지
* value function 과 마찬가지로 여기서도 first visit mc method, every visit mc method 가 있을 것
	* 근데 episode 가 많아지면 수렴해서 뭘 쓰던 상관이 없지
* mc를 이용할 경우 deterministic policy 를 사용하게 되면 state X 에 대해 정해진 policy 로만 움직이기 때문에 아무리 많은 episode 를 반복해도 이런 경우에 대한 값은 구할 수가 없어
	* stochastic policy 를 써야지

* Control problem
	* Policy iteration : sweep through state space until converge
	* Truncated policy iteration : do fixed number of sweeps through state space
	* Value iteration : do one sweep through state space
* Generalized policy iteration
	* 위의 세계에서 common한 요소들
	* Action value 를 Update 할 때 episode 다 끝나고 하는게 아니고 등장할때마다 iterative 하게 update 해나가