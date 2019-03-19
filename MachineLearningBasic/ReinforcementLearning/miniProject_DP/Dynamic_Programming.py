
# coding: utf-8

# # Mini Project: Dynamic Programming
from frozenlake import FrozenLakeEnv

env = FrozenLakeEnv()

print(env.observation_space)
print(env.action_space)

# print the total number of states and actions
print(env.nS)
print(env.nA)


print(env.P[1][0])
print(env.P[1][0][0])
print(env.P[1][0][0][2])

#print(env.P)
for i in range(env.nA):
    print(env.P[14][i])
    
'''for a in range(env.nS):
    print(a)
    for b in env.P[a]:
        print("##"+str(b))
        print(env.P[a][b])'''


import numpy as np
#1e-8
def policy_evaluation(env, policy, gamma=1, theta=0.0000001):
    V = np.zeros(env.nS, dtype='float')

    while 1:
        V_next = np.zeros(env.nS, dtype='float')
        for i in range(env.nS):
            #V_next=V
            for j in range(env.nA):
                policy_prob=policy[i][j]
                #print(str(i)+", "+str(j))
                #print(policy_prob)
                if policy_prob==0.0:
                    print("pass")
                    continue
                for probability, next_state, reward, done in env.P[i][j]:
                    #print(policy_prob*probability*(reward+V[next_state]*gamma))
                    #print(reward+V[next_state]*gamma)
                    V_next[i]+=policy_prob*probability*(reward+V[next_state]*gamma)
                    #print("###")
                    #print(V_next[i])
                    #print("###")
        #print(V_next)
        #print(np.abs(V - V_next).max())
        if np.abs(V - V_next).max() >= theta:
            V=V_next
        else:
            break;
    return V



random_policy = np.ones([env.nS, env.nA]) / env.nA
print(random_policy)

from plot_utils import plot_values

# evaluate the policy 
V = policy_evaluation(env, random_policy)

plot_values(V)



import check_test

check_test.run_check('policy_evaluation_check', policy_evaluation)


def q_from_v(env, V, s, gamma=1):
    q = np.zeros(env.nA)#state s 에서 action 을 했을 때에 얻을 수 있는 기대값
    for a in range(env.nA):
        for probability, next_state, reward, done in env.P[s][a]:
            q[a]+=probability*(reward + V[next_state]*gamma)
    return q


Q = np.zeros([env.nS, env.nA])
for s in range(env.nS):
    Q[s] = q_from_v(env, V, s)
print("Action-Value Function:")
print(Q)



check_test.run_check('q_from_v_check', q_from_v)


def policy_improvement(env, V, gamma=1):
    policy = np.zeros([env.nS, env.nA]) / env.nA
    for s in range(env.nS):
        q=q_from_v(env, V, s, gamma)
        #print(np.argwhere(q==np.max(q)))
        max_index=np.argwhere(q==np.max(q)).flatten()
        #print([np.eye(env.nA)[1],np.eye(env.nA)[2]])
        #print(np.sum([np.eye(env.nA)[i] for i in max_index], axis=0)/len(max_index))
        policy[s] = np.sum([np.eye(env.nA)[i] for i in max_index], axis=0)/len(max_index)
        #policy[s]=q/q.sum(axis=0, keepdims=1)
        #print(policy[s])
    return policy



check_test.run_check('policy_improvement_check', policy_improvement)

import copy

def policy_iteration(env, gamma=1, theta=1e-8):
    policy = np.ones([env.nS, env.nA]) / env.nA
    while 1:
        V=policy_evaluation(env, policy, gamma, theta)
        policy_new=policy_improvement(env, V, gamma)
        if np.abs(policy - policy_new).max() >= theta:
            policy=policy_new
        else:
            break;
    
    return policy, V

policy_pi, V_pi = policy_iteration(env)

print("\nOptimal Policy (LEFT = 0, DOWN = 1, RIGHT = 2, UP = 3):")
print(policy_pi,"\n")

plot_values(V_pi)



check_test.run_check('policy_iteration_check', policy_iteration)



def truncated_policy_evaluation(env, policy, V, max_it=1, gamma=1):
    num_it=0
    while num_it < max_it:
        for s in range(env.nS):
            v = 0
            q = q_from_v(env, V, s, gamma)
            for a, action_prob in enumerate(policy[s]):
                v += action_prob * q[a]
            V[s] = v
        num_it += 1
    return V



def truncated_policy_iteration(env, max_it=1, gamma=1, theta=1e-8):
    V = np.zeros(env.nS)
    policy = np.zeros([env.nS, env.nA]) / env.nA
    while True:
        policy = policy_improvement(env, V)
        old_V = copy.copy(V)
        V = truncated_policy_evaluation(env, policy, V, max_it, gamma)
        if max(abs(V-old_V)) < theta:
            break;
    return policy, V



policy_tpi, V_tpi = truncated_policy_iteration(env, max_it=2)


print("\nOptimal Policy (LEFT = 0, DOWN = 1, RIGHT = 2, UP = 3):")
print(policy_tpi,"\n")

plot_values(V_tpi)


check_test.run_check('truncated_policy_iteration_check', truncated_policy_iteration)


def value_iteration(env, gamma=1, theta=1e-8):
    V = np.zeros(env.nS)
    while True:
        delta = 0
        for s in range(env.nS):
            v = V[s]
            V[s] = max(q_from_v(env, V, s, gamma))
            delta = max(delta,abs(V[s]-v))
        if delta < theta:
            break
    policy = policy_improvement(env, V, gamma)
    return policy, V

policy_vi, V_vi = value_iteration(env)

print("\nOptimal Policy (LEFT = 0, DOWN = 1, RIGHT = 2, UP = 3):")
print(policy_vi,"\n")


plot_values(V_vi)



check_test.run_check('value_iteration_check', value_iteration)

