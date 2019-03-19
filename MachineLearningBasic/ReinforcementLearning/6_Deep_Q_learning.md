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


# Deep Q network
* 때에따라 policy 가 (state 와 action 간에 큰 상관관계가 있을 때에 등) oscillation 이나 diverge 할 수 있음
	* Experience replay
	* Fixed Q targets
* Experience replay
	* Replay buffer 에 agent 가 행했던 (St, At, Rt+1, St+1) 의 tuple 을 버리지 않고 저장해 둬
	* 다음 learning 을 할때에 이 중에 몇개를 sample 해서 learn 해
	* Rare 하게 발생하는 일도 잘 learn 할 수 있음
	* State 와 action 간의 큰 상관관계가 있더라도 이 완벽하게 순서대로 learn 하지 않기 때문에 괜찮아(진동, 발산을 막을 수 있음)
	* Reinforcement learning -> supervised learning 처럼 이용할 수 있게 바꿔줘
	* Prioritized experience replay
		* Rare 하게 발생하는 상황이나, 더 중요한 상황에 대해서 가중치를 줄 수있어
	* Problems between consecutive experience tuples
* Fixed Q targets
	* Q-learning a form of TD learning
	* Derivative 구해서 gradient descent 로 update
	* 근데 여기서 얻은 q_pie 를 바로 아래의 식에 대응시키는거는 수학적으로 맞지 않아
	* 구하려는 delta w와 바꾸려는 w 가 동일하거든;;
	* w- 사용:  w- 는 learning step 에서 바꾸지 않음
* Algorithm: Deep Q-learning
	* Sample and learning step
		* Sample : action 하면서 환경을 sample 함. observed experienced tuples 을 저장해 나감
		* Learning : 이 메모리에 저장된 sample 에서 random 하게 small batch 를 선택하고 이 batch 에서 gradient descent 통해서 step update 를 학습함
		* 이 두 step 은 직접적인 상관관계가 없어서 sample 을 여러번에 learning 한번, 아님 그 반대로 막 조합해서 해도 다 말이 돼
* DQN Imprivements
	* Double DQNs
	* Prioritized replay
	* Dueling networks
* Overestimation of Q-values
	* Action with max Q-value 구하는 데에서 실수가 생길 수 있음
		* 이 이전까지의 step 이 충분하지 않았다면
		* (어떤 action 을 해 왔는지, 어떤 neighboring state 를 거쳐왔는지가 중요해짐)
		* 이 노이지한 숫자들 중에 max 를 선택하게 되니깐 문제가 생길 수 있지
	* Double Q learning
		* Best action 을 select 할 때의 w 와 action을 evaluate 을 하는 w를 서로 다르게
		* 앞에서 사용했던 w-를 여기서도 사용
		* 요것만 바꿔도 vanila dqn 보다 성능이 좋아!
* Experience replay 이용하는 상황에서
	* 다른 것 보다 더 중요하고 rare 한 상황이 있을 경우 --> 이 중요한 event 들 마저 buffer 안에서 uniformly select 된다면 선택되게될 확률이 아주 적어져
	* Prioritized replay
		* TD error 가 크다면 그 tuple 에서 더 많은걸 배워야 할 것
		* Buffer 의 td error 값을 같이 저장해둬
		* + td error 가 0 이면 learning 에 안들어갈거야 -> priority 에 작은 상수를 더해줘
		* 반복되는 몇개의 subset 은 계속 무시될거야 (overfitting 될 것)
			* 변수 a 를 놓아 (a 가 0이면 uniform,  1이면 priority 만 사용하게 될 것)
* Dueling networks



