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
``` python
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
        state=env.reset()
        while True:
            action=policy[state]
            next_state, reward, done, info=env.step(action)
            V[state]=V[state]+(alpha *(reward +(gamma*V[next_state])-V[state]))
            state=next_state
            if done:
                break
    return V 
```
* TD Control : Sarsa(0)
	* Sarsa(0) : on-policy TD control method
		* 이전에 MC 에서 했듯이 epsilon 이용해서 greedy 여부 결정
	* optimal action-value function q* 로의 수렴을 보장함
	(alpha 가 충분히 작고, epsilon 이 GLIE 를 만족하게 setting 되어있다면)
``` python
import matplotlib.pyplot as plt
%matplotlib inline
def update_Q(Qsa, Qsa_next, reward, alpha, gamma):
    """ updates the action-value function estimate using the most recent time step """
    return Qsa + (alpha * (reward + (gamma * Qsa_next) - Qsa))

def epsilon_greedy_probs(env, Q_s, i_episode, eps=None):
    """ obtains the action probabilities corresponding to epsilon-greedy policy """
    epsilon = 1.0 / i_episode
    if eps is not None:
        epsilon = eps
    policy_s = np.ones(env.nA) * epsilon / env.nA
    policy_s[np.argmax(Q_s)] = 1 - epsilon + (epsilon / env.nA)
    return policy_s

def sarsa(env, num_episodes, alpha, gamma=1.0):
    # initialize action-value function (empty dictionary of arrays)
    Q = defaultdict(lambda: np.zeros(env.nA))
    # initialize performance monitor
    plot_every = 100
    tmp_scores = deque(maxlen=plot_every)
    scores = deque(maxlen=num_episodes)
    # loop over episodes
    for i_episode in range(1, num_episodes+1):
        # monitor progress
        if i_episode % 100 == 0:
            print("\rEpisode {}/{}".format(i_episode, num_episodes), end="")
            sys.stdout.flush()   
        # initialize score
        score = 0
        # begin an episode, observe S
        state = env.reset()   
        # get epsilon-greedy action probabilities
        policy_s = epsilon_greedy_probs(env, Q[state], i_episode)
        # pick action A
        action = np.random.choice(np.arange(env.nA), p=policy_s)
        # limit number of time steps per episode
        for t_step in np.arange(300):
            # take action A, observe R, S'
            next_state, reward, done, info = env.step(action)
            # add reward to score
            score += reward
            if not done:
                # get epsilon-greedy action probabilities
                policy_s = epsilon_greedy_probs(env, Q[next_state], i_episode)
                # pick next action A'
                next_action = np.random.choice(np.arange(env.nA), p=policy_s)
                # update TD estimate of Q
                Q[state][action] = update_Q(Q[state][action], Q[next_state][next_action], 
                                            reward, alpha, gamma)
                # S <- S'
                state = next_state
                # A <- A'
                action = next_action
            if done:
                # update TD estimate of Q
                Q[state][action] = update_Q(Q[state][action], 0, reward, alpha, gamma)
                # append score
                tmp_scores.append(score)
                break
        if (i_episode % plot_every == 0):
            scores.append(np.mean(tmp_scores))
    # plot performance
    plt.plot(np.linspace(0,num_episodes,len(scores),endpoint=False),np.asarray(scores))
    plt.xlabel('Episode Number')
    plt.ylabel('Average Reward (Over Next %d Episodes)' % plot_every)
    plt.show()
    # print best 100-episode performance
    print(('Best Average Reward over %d Episodes: ' % plot_every), np.max(scores))
    return Q
```
* TD Control : Sarsamax
	* (= Q-learning)
	* Off-policy method
	* Optimal action value function Q*
	* salsa control algorithm 에서 converge 되는 조건에서 얘도 converge 됨
``` python
def q_learning(env, num_episodes, alpha, gamma=1.0):
    # initialize action-value function (empty dictionary of arrays)
    Q = defaultdict(lambda: np.zeros(env.nA))
    # initialize performance monitor
    plot_every = 100
    tmp_scores = deque(maxlen=plot_every)
    scores = deque(maxlen=num_episodes)
    # loop over episodes
    for i_episode in range(1, num_episodes+1):
        # monitor progress
        if i_episode % 100 == 0:
            print("\rEpisode {}/{}".format(i_episode, num_episodes), end="")
            sys.stdout.flush()
        # initialize score
        score = 0
        # begin an episode, observe S
        state = env.reset()
        while True:
            # get epsilon-greedy action probabilities
            policy_s = epsilon_greedy_probs(env, Q[state], i_episode)
            # pick next action A
            action = np.random.choice(np.arange(env.nA), p=policy_s)
            # take action A, observe R, S'
            next_state, reward, done, info = env.step(action)
            # add reward to score
            score += reward
            # update Q
            Q[state][action] = update_Q(Q[state][action], np.max(Q[next_state]), \
                                                  reward, alpha, gamma)        
            # S <- S'
            state = next_state
            # until S is terminal
            if done:
                # append score
                tmp_scores.append(score)
                break
        if (i_episode % plot_every == 0):
            scores.append(np.mean(tmp_scores))
    # plot performance
    plt.plot(np.linspace(0,num_episodes,len(scores),endpoint=False),np.asarray(scores))
    plt.xlabel('Episode Number')
    plt.ylabel('Average Reward (Over Next %d Episodes)' % plot_every)
    plt.show()
    # print best 100-episode performance
    print(('Best Average Reward over %d Episodes: ' % plot_every), np.max(scores))
    return Q
```
* TD Control : Expected Sarsa
	* On-policy method
	* Optimal action value function Q*
	* salsa control algorithm 에서 converge 되는 조건에서 얘도 converge 됨
``` python
def expected_sarsa(env, num_episodes, alpha, gamma=1.0):
    # initialize action-value function (empty dictionary of arrays)
    Q = defaultdict(lambda: np.zeros(env.nA))
    # initialize performance monitor
    plot_every = 100
    tmp_scores = deque(maxlen=plot_every)
    scores = deque(maxlen=num_episodes)
    # loop over episodes
    for i_episode in range(1, num_episodes+1):
        # monitor progress
        if i_episode % 100 == 0:
            print("\rEpisode {}/{}".format(i_episode, num_episodes), end="")
            sys.stdout.flush()
        # initialize score
        score = 0
        # begin an episode
        state = env.reset()
        # get epsilon-greedy action probabilities
        policy_s = epsilon_greedy_probs(env, Q[state], i_episode, 0.005)
        while True:
            # pick next action
            action = np.random.choice(np.arange(env.nA), p=policy_s)
            # take action A, observe R, S'
            next_state, reward, done, info = env.step(action)
            # add reward to score
            score += reward
            # get epsilon-greedy action probabilities (for S')
            policy_s = epsilon_greedy_probs(env, Q[next_state], i_episode, 0.005)
            # update Q
            Q[state][action] = update_Q(Q[state][action], np.dot(Q[next_state], policy_s), \
                                                  reward, alpha, gamma)        
            # S <- S'
            state = next_state
            # until S is terminal
            if done:
                # append score
                tmp_scores.append(score)
                break
        if (i_episode % plot_every == 0):
            scores.append(np.mean(tmp_scores))
    # plot performance
    plt.plot(np.linspace(0,num_episodes,len(scores),endpoint=False),np.asarray(scores))
    plt.xlabel('Episode Number')
    plt.ylabel('Average Reward (Over Next %d Episodes)' % plot_every)
    plt.show()
    # print best 100-episode performance
    print(('Best Average Reward over %d Episodes: ' % plot_every), np.max(scores))
    return Q
```
* Analyzing Performance
	* On-policy TD control method (Expected Sarsa & Sarsa)
		* better online performance than off-policy TD control method
		* Expected Sarsa 가 보통 Sarsa 보다 성능이 나아
