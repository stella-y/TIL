## Unsupervised Reinforcement Learning
* 학습을 하고, 이걸 represent 하는게 generalizing 을 더 좋게 해주더라
* Intrinsic Motivation
	* Unsupervised learning --> policy of RL agent 를 좀 더 가이드하는 역할을 하게 됨 + representation 능력을 더 높여주더라
	* 명확한 award 가 없더라도 agent intrinsically motivated 되더라…
	* 다양하게 존재하고, 동의된 하나의 형식은 없더라…
* Curious agents
	* Intrinsic motivation 의 하나로 Agent 를 호기심가득하게 만드는 방법
		* Novel observation 을 얻을 수 있는 방향으로 agent 가 움직일 수 있도록 --> 더 빠르게 학습해나가게 하기 위해서
		* Curiosity-driven exploration by self-supervised prediction
			* Unpredictable 한 latent value 를 주는 장소로 이동하게 하는 것
			* Prediction error 를 최대화 시키는 곳으로 가게 하는 action 을 취하게 함
			* Noise addiction problem 발생할 것 )noise 가 계속 더해질 수가 있을 것) --> prediction 을 latent space 안에서만 하게 함(latent representation 로는 노이즈가 들어가지 않게 됨)
		* Bayesian Surprise : posterior 와 prior 사이의 kl divergence 를 최대가 되게 만든다
		* Prediction gain : baysian surprise를 근사시켜서 
		* Curiouser and curiouser…
			* Complexity gain 대신 compression progress 라고 불려야 한다고 함
			* 그 데이터로부터 뭔갈 배울 수 있게 도와주는 데이터를 찾아다니는게 아니고, 모든 걸 알 수 있게 해주는 데이터를 찾아가게 됨
				
				
* Empowered agents
	* Agent 의 action 과 action으로 받는 결과사이에 mutual information 을 극대화 시키게 함 - 앞으로 벌어질 일에 더 control 할 수 있는 능력을 크게 갖게 되는 것
	* Curious agent 가 한번에 모든걸 다 알려고 하는 학생 같다면, empowered agent 는 움직이려하지 않지만 멀리서보면서 더 크게 컨트롤하고자 하는 늙은이 같다고 함
		
		
* Conclusion
	* 어디서 뭘 배워야 하는지에 대한 signal 을 주게 됨
	* 하지만 학습해야할 대상이 명확하지 않음
	* --> density model 이 그 option 이 될 수 있음
	* Auto regressive neural network 가 density model 중 하나라고 볼 수 있음
	* Autoencoding 이나 predictive coding 이 유용한 latent representation 을 생성해줄 수 있음
	* 강화학습도, unsupervised learning 으로부터 도움을 받을 수 있음
		* Auxiliary loss / 아니면 curiosity 등 같은 intrinsic 한 motivation signal 을 줄 수있음
