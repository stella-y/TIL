* atari game / go game

* 강화학습을 푼다  최적의 정책 함수를 찾는 것
이 최적의 정책 함수는 불확실한 미래에 얻을 수 있는 보상 함수의 기대값을 최대로 하는 행동을 매번 고른다

atari game

Policy
주어진 시간에 agent 의 behavior
Reward signal
그때그때 환경으로부터 받는 feed back
Value function
장기적인 reward 의 측정
State 의 value : 그 state 에서 시작해서 미래까지 받을 수 있는 reward 의 총합 측정
Model
환경의 behavior 를 모방 도는 환경의 behave 를 추정


mdp 정의

* episode
	Episode
Situation, action, reward 의 반복 / 
이 과정의 처음부터 끝까지의 interaction 을 episode 라고 불러
Well defined ending point 경우를 말함

optimality principle & dynamic programming
 --> dynamic programing

Q learning
--> model free learning


model based learning
--> deep reinforcement learning

DQN
--> q-network 썼는데도 잘 안되던 문제들 해결
깊은 network 
--> experience replay
--> stationary 할 수 있게, 미분 대상과 변화 대상을 분리시켜 / 

