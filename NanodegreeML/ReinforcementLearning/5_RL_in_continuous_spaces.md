# RL in continuous spaces
* Reinforcement learning : frame work
	* MDP(Markov Decision Process)
		* state transition and reward model
		* state value function
		* acton value function
	* goal : Find optimal policy pie* that maximizes total expected reward

* Reinforcement learning : algorithms
	* Model based learning (dynamic programming)
		* policy iteration
		* value iteration
	* Model free learning
		* Monte Carlo Methods
		* Temporal-Difference learning

* Discrete spaces
	* 이전까지는 다 discrete 한 상황을 가정했음
	* state, state*action pair 모두 유한함을 가정하고 function 설계
	* 이게 무한해지면 다룰 수 없게 되지(Q-learning 도 마찬가지)
* Countinuous space 에서
	* 실제 상황은 여기에 더 가까움
	* descritization/ function approximation 등의 방법 사용해야
	