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
