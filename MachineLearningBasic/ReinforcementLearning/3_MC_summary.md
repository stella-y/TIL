# MC steps
1. MC prediction: state values
	* policy 가 pie일 때 V_pie 구하는 문제
	* policy pie 를 평가하는 방법 두가지
		1. on-policy
			* agent 가 주어진 동일한 policy 를 따라가면서 evaluate or improve
		2. off-policy
			* 현재의 policy 와 또다른 policy 를 따라가면서 evaluate or improve
			* 여러 episode 들을 value function estimation 에 사용함
			* 각 episode, 각 state 에서 얻게 되는 reward 의 값을 평균 내서 그 state의 valuefunction 으로 이용(first-visit or every-visit)
	* Monte Carlo prediction method 두가지
		1. first-visit MC : V_pie(s)계산시 s 에 대해서 오로지 첫번째 방문만의 return 의 average 계산
		2. every-visit MC : S를 방분할때 얻은 모든 return 들을 평균내서 value function 에 이용
	``` python
	def mc_prediction_v(env, num_episodes, generate_episode, gamma=1.0):
	    # initialize empty dictionary of lists
	    returns = defaultdict(list)
	    # loop over episodes
	    for i_episode in range(1, num_episodes+1):
	        # monitor progress
	        if i_episode % 1000 == 0:
	            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
	            sys.stdout.flush()
	        episode=generate_episode(env)
	        #print(episode)        
	        states, actions, rewards=zip(*episode)
	        discounts = np.array([gamma**i for i in range(len(rewards)+1)])
	        #print(rewards)
	        for i, s in enumerate(states):
	            returns[s].append(sum(rewards[i:]*discounts[:-(1+i)]))
	    V= {k: np.mean(v) for k, v in returns.items()}
	    return V
	```
2. MC prediction : Action value
	* q(s,a) 구하기 (action value)
		* first-visit mc : Q_pie(s,a) 구할 때 처음으로 방문한 s,a 만을 고려하여 계산
		* every-visit mc : 다 고려
	* 정해진 policy 만으로 움직이면 다른 가능성 계산이 어려움(나중에 evaluation 이 안되겠지) --> stochastic 하게 방문하도록 한다
	``` python
	def generate_episode_from_limit_stochastic(bj_env):
	    episode = []
	    state = bj_env.reset()
	    while True:
	        probs = [0.8, 0.2] if state[0] > 18 else [0.2, 0.8]
	        action = np.random.choice(np.arange(2), p=probs)
	        next_state, reward, done, info = bj_env.step(action)
	        episode.append((state, action, reward))
	        state = next_state
	        if done:
	            break
	    return episode
	```
	* q function 만들기
	``` python
	def mc_prediction_q(env, num_episodes, generate_episode, gamma=1.0):
	    # initialize empty dictionaries of arrays
	    returns_sum = defaultdict(lambda: np.zeros(env.action_space.n))
	    N = defaultdict(lambda: np.zeros(env.action_space.n))
	    Q = defaultdict(lambda: np.zeros(env.action_space.n))
	    # loop over episodes
	    for i_episode in range(1, num_episodes+1):
	        # monitor progress
	        if i_episode % 1000 == 0:
	            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
	            sys.stdout.flush()
	        episode=generate_episode(env)
	        states, actions, rewards=zip(*episode)
	        #discount
	        discounts=np.array([gamma**i for i in range(len(rewards)+1)])
	        for i, state in enumerate(states):
	            returns_sum[state][actions[i]]+=sum(rewards[i:]*discounts[:-(1+i)])
	            N[state][actions[i]]+=1.0
	            Q[state][actions[i]]=returns_sum[state][actions[i]]/N[state][actions[i]]
	    return Q
	```
3. Generalized policy iteration
	* control problem - optimal policy pie\* 를 결정하는게 목표
		* Policy iteration : sweep through state space until converge
		* Truncated policy iteration : do fixed number of sweeps through state space
		* Value iteration : do one sweep through state space
	* GPI 는 policy 를 evaluate하고, improve 하는 전체의 과정임
		* action value 를 update 할 때에 episode 다 끝나고 하는게 아니고 iterative 하게 update 되도록!
4. MC control
	1. Incremental mean
		* Derive an algorithm that keeps a running average of a sequence of numbers
		* action value 를 update 할 때에 episode 다 끝나고 하는게 아니고 iterative 하게 update 되도록!
	2. Policy Evaluation
		* 1개의 episode 가 끝날 때 마다 policy 를 평가할 수 있도록
	3. Policy Improvement
		* GLIE
			* Based on Exloration-Exloitation Dilemma
		* 다음 action 을 선택할 때에 greedy 하게 action value 가 최대인 root 로 갈 수 있겠지만 이렇게 되면 방문했던 노드만을 방문하게 됨
		* epsilon greedy
			* 1-epsilon 확률만큼 greedy 한 action 으로
			* epsilon 확률 만큼 random 하게(uniformly)
			* 입실론이 
				* 0이면 항상 random하게 선택
				* 1이면 어떤 상황에서도 균등하게 선택 됨(equiprobable random policy)
				* epsilon > 0 :  the agent has nonzero probability of selecting any of the available actions.
				* 근데 항상 greedy 인 경우는 없어
	``` python
	def generate_episode_from_Q(env, Q, epsilon, nA):
	    """ generates an episode from following the epsilon-greedy policy """
	    episode = []
	    state = env.reset()
	    while True:
	        action = np.random.choice(np.arange(nA), p=get_probs(Q[state], epsilon, nA)) \
	                                    if state in Q else env.action_space.sample()
	        next_state, reward, done, info = env.step(action)
	        episode.append((state, action, reward))
	        state = next_state
	        if done:
	            break
	    return episode
	def get_probs(Q_s, epsilon, nA):
	    """ obtains the action probabilities corresponding to epsilon-greedy policy """
	    policy_s = np.ones(nA) * epsilon / nA
	    best_a = np.argmax(Q_s)
	    policy_s[best_a] = 1 - epsilon + (epsilon / nA)
	    return policy_s
	def update_Q_GLIE(env, episode, Q, N, gamma):
	    """ updates the action-value function estimate using the most recent episode """
	    states, actions, rewards = zip(*episode)
	    # prepare for discounting
	    discounts = np.array([gamma**i for i in range(len(rewards)+1)])
	    for i, state in enumerate(states):
	        old_Q = Q[state][actions[i]] 
	        old_N = N[state][actions[i]]
	        Q[state][actions[i]] = old_Q + (sum(rewards[i:]*discounts[:-(1+i)]) - old_Q)/(old_N+1)
	        N[state][actions[i]] += 1
	    return Q, N
	def mc_control_GLIE(env, num_episodes, gamma=1.0):
	    nA = env.action_space.n
	    # initialize empty dictionaries of arrays
	    Q = defaultdict(lambda: np.zeros(nA))
	    N = defaultdict(lambda: np.zeros(nA))
	    # loop over episodes
	    for i_episode in range(1, num_episodes+1):
	        # monitor progress
	        if i_episode % 1000 == 0:
	            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
	            sys.stdout.flush()
	        epsilon=1.0/((i_episode/8000)+1)
	        episode=generate_episode_from_Q(env,Q,epsilon, nA)
	        Q, N=update_Q_GLIE(env, episode, Q, N, gamma)
	    policy=dict((k, np.argmax(v)) for k, v in Q.items())
	    return policy, Q
	```
	5. Constant-alpha
		* learning 의 속도를 결정
			* 실제의 return 이 G_t 이고, 예상한 return 이 Q(S_t, A_t) 인 것
			* Delta 가 0보다 크면 Q 는 늘어야하고, 작으면 Q 는 작아져야 하는데 그 커지고 작아지는 비율이 proportional to 1/(N(S_t, A_t))
			* 횟수를 거듭할수록 이 비율이 줄어들 수밖에 없지
		* 1/(N(S_t, A_t)) 이거 대신 상수 alpha를 곱해서 learning 속도가 느려지지 않도록 해
		* 0 < alpha <= 1
		* 클수록 빨리 learning 하되 수렴하지 않을것
	```python
	def update_Q_alpha(env, episode, Q, alpha, gamma):
	    states, actions, rewards=zip(*episode)
	    discounts=np.array([gamma**i for i in range(len(rewards)+1)])
	    for i, state in enumerate(states):
	        old_Q=Q[state][actions[i]]
	        Q[state][actions[i]]=old_Q + alpha*(sum(rewards[i:]*discounts[:-(1+i)])-old_Q)
	        return Q
	def mc_control_alpha(env, num_episodes, alpha, gamma=1.0):
	    nA = env.action_space.n
	    # initialize empty dictionary of arrays
	    Q = defaultdict(lambda: np.zeros(nA))
	    # loop over episodes
	    for i_episode in range(1, num_episodes+1):
	        # monitor progress
	        if i_episode % 1000 == 0:
	            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
	            sys.stdout.flush()
	        epsilon=1.0/((i_episode/8000)+1)
	        episode=generate_episode_from_Q(env, Q, epsilon, nA)
	        Q=update_Q_alpha(env, episode, Q, alpha, gamma)
	    policy=dict((k, np.argmax(v)) for k, v in Q.items())
    return policy, Q
	```
