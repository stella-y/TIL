* Reinforcement learning 에 neural net 쓰기 위해서 필요
* Neural Network as Value Functions
	* 각 단계에서 loss 를 계산해서 다음 w update 해서 다음 loss 를 구해야하는데, 진짜 value 를 알 수가 없어!(이걸 알아야 loss 계산을 하지...)
	* monte carlo learning
		* Cumulative discounted reward on a current time t 
		* every visit 일 때
		```
		- initialize w with random value
		- initialize policy : pie <-- epsilon greedy(q(s,a,w))
		- repeat till convergence:
			evalueation :
				generate an episode s0, a0, r1, ..., sr using pie
				for t <- 1 to T:
					delta_w=a(G_t-q(st, at, w))q(st, at, w)
			improvement :
				pie <- epsilon-greedy(q(s,a,w))
		```
	* Q-learning
		* Update step 이 다르지
			* Action greedly / update 할 때만 쓰지 실제로 이렇게 이동하는건 아니야

* Sarsa vs q-learning
	* Sarsa
		* On-policy- learning 하고 있는 policy 만 따름
		* Good online performance(online learning 에 더 유리함)
		* Q-values affected by exploration
	* Q-learning
		* Off-policy(learning 하고 있는 policy 랑 action 이랑 다를 수 있음)
		* Bad online performace(following 하는 action 과 policy 가 다를 수 있기 때문에)
		* Q-values unaffected by exploration
*장단이 명확해서 쓰려는 환경에 따라 뭐 쓸건지 잘 고르면 좋아*

* Off-policy advantages
	* More exploration when learning
	* Learning from demonstration
	* Supports offline or batch learning
