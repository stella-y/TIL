## Document Level Models
	• Document level language modeling
		○ 전체 문서 안에서 단어의 확률을 예측하는 것
		○ Modeling using recurrent networks
			§ 이전의 정보를 hidden state 로 passing 하는 모델
		○ Separate Encoding for Coarsegrained Document Context 
			§ 하나의 큰 lstm 은 global context 를 놓치는 경우가 많더라
		○ 문제점이 네가지가 있음
			§ 이 중에 하나 --> 지시어 문제(coreference)
			
	• Coreference 문제에서
		○ 뉴럴넷을 쓸때의 장점
			§ Feature 들을 learning 해준다(feature selection 등을 따로 할 필요가 없지)
			§ Metric 을 대상으로 직접 학습할 수 있게 된다
			§ Jointly perform mention detection and clustering - 
		○ Coreference Resolution w/ EntityLevel Distributed Representations
			§ Mention pair
				□ 
			§ 이것들이 cluster
				□ 
				□ Intra 되는 cluster 에서의 element 끼리만 pair 를 만들어서 학습시킴
				□ 이걸 pooling 시켜서, cluster representation
				□ 이게 되고 나면 cluster 끼리의 유사성을 기반으로 
			§ Deep Reinforcement Learning for Mention-Ranking Coreference Models
				□ 강화학습을 이용
					® Previous antecedent is considered as an action of the agent
	• Cluster features with Neural Network
	• End-to-End Neural Coreference
		○ Lee et.al (2017)
			§ Coreference 를 알아내는 문제를 푸는것이 mention detection 을 알아내는데에 기여를 해 줄 것인가
			§ Span model
				□ Feature 간의 correlation 을 구하는 것
					® 
					® Feature 두개를 올리고, 이 둘 간의 연관관계를 가운데로 올림
					® 근데 어떤 경우에 두개의 pair, 어떤 경우에 3개의 pair 를 구성하게 되는지는 논문을 봐야알 것 같음
			§ Coreference Model
				□ 
				□ Span representation 이 나오면, mention 인지 score 를 매기고, 다시 이들끼리 coreference 관계에 있는지 score 를 매겨버림
				□ 맨위의 softmax 는 평가하기 위한 지표같은 것
		○ Using Coreference in Neural Models
			§ Coreference 를 뉴럴넷으로 한다면 가능해지는 것들
			§ Co-reference aware language modeling(Yang et al. 2017)
			§ Co-reference aware QA models (Dhingra et al. 2017)
	• Discourse parsing
		○ 어떤걸 어떻게 하는지에 대한 지시를 알려주는 것
		○ 
			
		○ Shift-reduce Parsing Discourse Structure Parsing w/ Distributed Representations (Ji and Eisenstein 2014)
			§ Queue, stack 의 명령어를 학습해서 한다고 생각하면 될 것
		○ Recursive Deep Models for Discourse Parsing Li et.al (2014)
			§ Tree 구조를 강화학습 이용해서 어떤 식일지를 학습하고 나서 
			§ Recursive NN for discourse parsing (similar to Socher’s recursive parsing) • First determine whether two spans should be merged (Binary) • Then determine the relation type
		○ Recursive NN for discourse parsing (similar to Socher’s recursive parsing)
			§ Li et.al (2016)
			§ First determine whether two spans should be merged (Binary) • Then determine the relation type
			§ 유행하는걸 다 넣은 것(attention 등)
		○ Implicit Discourse Connection Classification w/ Adversarial Objective (Qin et al. 2017)
			§ Not explicitely 인 경우를 학습하기 위해 because, however 등이 나왔던 문장으로 넣어서 gan style 로 학습함
			§ Discourse Connection을 써서 text classification 하는게 의미가 있더라
			§ & discourse parsing 의 result 가 classification 성능에 큰 영향을 끼치더라
