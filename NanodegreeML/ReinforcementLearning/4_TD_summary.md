# Temporal-Difference Method
* TD prediction : TD(0)
	* montecarlo 에서는 episode 가 끝나기까지를 기다려야 최선의 value function 을 얻어낼 수 있음
	* Temporal-difference method 는 value function 을 매 time step 마다 update 함
	* One-step TD (TD(0))
		step size parameter alpha 가 충분히 작다면 true state-value function 으로 항상 수렴한다
	* 실험적으로 TD prediction 이 MC prediction 보다 빠르게 수렴함
	* TD target = (Reward_(t+1)+ gamma * Value(State_(t+1))
	* previous estimate = Value(State_t)
	* V(State_t)=Previous estimate + alpha\*(TD target - previous estimate)
	``` scala
	from collections import defaultdict, deque
	import sys
	def td_prediction(env, num_episodes, policy, alpha, gamma=1.0):
    	# initialize empty dictionaries of floats
    	V = defaultdict(float)
    	# loop over episodes
    	for i_episode in range(1, num_episodes+1):
	        # monitor progress
	        if i_episode % 100 == 0:
	            print("\rEpisode {}/{}".format(i_episode, num_episodes), end="")
	            sys.stdout.flush()
	        # begin an episode, observe S
	        state = env.reset()
	        while True:
	            # choose action A
	            action = policy[state]
	            # take action A, observe R, S'
	            next_state, reward, done, info = env.step(action)
	            # perform updates
	            V[state] = V[state] + (alpha * (reward + (gamma * V[next_state]) - V[state]))            
	            # S <- S'
	            state = next_state
	            # end episode if reached terminal state
	            if done:
	                break   
    	return V
	```

* TD Prediction : Action Values
	* 이전까지는 state 정한 다음 그 state 의 value 를 update 하는 방식이었다면 이제는 action 을 행한 후 action value function 을 업데이트 하는 방식으로
	* TD(0)처럼 alpha 가 충분히 작다면 수렴함

* TD Control : Sarsa(0)
	* Sarsa(0) : on-policy TD control method
		* 이전에 MC 에서 했듯이 epsilon 이용해서 greedy 여부 결정
	* optimal action-value function q* 로의 수렴을 보장함
	(alpha 가 충분히 작고, epsilon 이 GLIE 를 만족하게 setting 되어있다면)


