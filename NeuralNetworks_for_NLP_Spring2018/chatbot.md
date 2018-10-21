## Neural Networks for NLP Models of Dialog and Conversation
챗봇!!
	• Models of chat
		○ 두개 패러다임 (generation-based model / retrieval based model)
			§ generation-based model --> 꿈꾸는 모델
				□ 기계가 질문에 대한 답을 그떄그때 만들어내는 것
				□ 나쁜 데이터에 쉽게 오염될 수 있음
			§ retrieval based model --> 가장 적합한 output 을 찾아서 내 놓음
				□ 자연어 질의를 던질 수 있는 검색이라고 보면 됨
				□ 안전함
		○ Generation based model((Ritter et al. 2011)
			§ 확률 기반으로 어떤 답을 생성할지 결정해 냄
			§ 
			§ 역사로만 알면 될 듯
		○ Neural Models for Dialog Response Generation
			§ (Sordoni et al. 2015, Sheng et al. 2015, Vinyals and Le 2015)
			§ Sequence to sequence 활용
			§ Like other translation tasks, dialog response generation can be done with encoder-decoders
			§ Sheng et al. (2015)
				□ 직전 발언만 사용
			§ 근데 이것의 문제점! --> 바로 앞 문장은 질문에 답을 하기에 충분한 정보를 가지고 있지 않을 수 있다!(context 필요)
				□ Sordoni et al. 2015 --> 전전 문장까지 넣자!
				□ Context --> 아직 연구 대상
				□ Vinyals et al. (2015) --> 전에 발생한 모든 문장 넣기
	• 근데 이것의 문제점! --> 바로 앞 문장은 질문에 답을 하기에 충분한 정보를 가지고 있지 않을 수 있다!(context 필요)
		○ Hierarchical Encoderdecoder Model 
			§ Serban et al. 2016
			§ Context 를 위한 rnn 을 만들어보자
			§ 
		○ Discourse-level VAE Model
			§ Zhao et al. 2017
			§ [영상 보고 캡쳐해보자]
			§ 
	• 상황에 맞는 좋은 답변이 나오게 (I don't know 보다 잘 나오도록)
		○ Diversity Promoting Objective for Conversation 
			§ Li et al. 2016
			§ 우리가 내 놓는 답변이 상황에 더 잘 맞는 답이었으면 좋겠다(범용보다는 특화된 답!)
			§ Tf/idf 와 유사
				□ Method: subtract weighted unconditioned log probability from conditioned probability (calculated only on first few words)
		○ Diversity is a Problem for Evaluation! 
			§ Dialog 에서는 정확한 답을 정해 놓는게 쉽지 않에서 bleu score 쓰기는 어려워
			§ Human score 만 가능
	• Evaluation 에 대한 연구 자체가 시작된게 얼마 안됐옹
		○ Using Multiple References with Human Evaluation Scores
			§ Galley et al. 2015
			§ 정답셋 만들기 + score 를 어떻게 낼 것인가에 대한 논의
		○ Evaluate 하는 것 자체를 학습하는 것
			§ 적은 데이터만으로 맞게 예측한다고 가정하는 모델을 만들어놓고, 
			§ Regressor 를 생성한 것 이 function 이 생성되고 나면 이걸 고정시켜 놓고 model response 와 비교하면서 학습시킴
			§ Overfit 이 좀 있는 단점이 있다고 함
	• Problem 3 : agent 에 personality 가 있길 바람
		답에 일관성이 있기도, 없기도


Retrieval-based Models
	• Retrieval-based Chat
		○ (Lee et al. 2009)
		○ 가장 그럴싸하게 답해주는 모델을 db 에서 찾아내는 식
	• Neural Response Retrieval
		○ Nio et al. 2014
		○ 뉴럴넷으로 retrieval
		○ 두 pair 의 문장에 대해서 similarity 를 측정하는 모델을 만들어서 query 에 대해서 가장 비슷한 답변을 가져오는 것
		○ 이거에 대한 활용은 뭐 많이 있을 수 있지
	• Smart Reply for Email Retrieval
		○ Kannan et al. 2016
		○ 구글에서 메일 시스템에 적용한 것
		○ Similar response model with LSTM seq2seq scoring, but many improvements 
			§ Beam search 
			§ Canonicalization of syntactic variants and clustering of similar responses --> 유사한 cluster 에서는 답을 하나만 내도록
			§ Human curation of responses 
			§ Enforcement of diversity through omission of redundant responses and enforcing positive/negative --> 긍/부정이 하나씩은 나오도록 

Task-driven dialog
	• 현재 ai 챗봇의 실체 / 실제로 working 하는 데에서는 다 이걸 씀
	• Traditional Task-completion Dialog Framework
		○ Natural language understanding
			§ 칸채우기 하는 구조 / 동일한 entity 가 동일하게 인식이 되도록
		○ Dialog state tracking
			§ 대화 진행상황 tracking --> 짱 어려운 문제랭
		○ Dialog control
			§ 상태에 따라서 dialog 를 다르게 냄
		○ Natural language generation
			§ 언어적으로 매끄럽게나올 수 있도록
	• Bio tagging system
		○ NLU (for Slot Filling) w/ Neural Nets 
		○ Mesnil et al. 2015
		○ Bio tagging : B 시작 I 계속 o 상관 없다
		○ RNN-CRF based model for tags
	• Dialog State Tracking
		○ Williams et al. 2013
		○ 못들었어! 라고 말하면 아까그 답을 반복해줄 수 있는 정도
	• Language Generation from Dialog State w/ Neural Nets (
		○ Wen et al. 2015
		○ Dialog act --> 이게 뭐 욕인지 답인지 질문인지 이런거 알아내기

		
	• End-to-end Dialog Control
		○ Williams et al. 2017
		○ 어떤 api 를 호출할지를 학습하는 것
		○ Train an LSTM that takes in text and entities and directly chooses an action to take (reply or API call)
		○ Trained using combination of supervised and reinforcement learning
		○ 
			
			

		
