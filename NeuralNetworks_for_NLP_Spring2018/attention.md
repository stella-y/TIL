	• Sentence 하나를 single vector 하나로 표현할 수는 없다! 라는 문제제기에서 출발
		○ 단어 하나마다 vector를 두는 식?
	• Attention
		○ Basic idea
			§ attention을 어디다 넣느냐도 사실은 design choice
		○ Calculating attention
			§ Sequence * hidden
			§ Attention 자체를 뽑는 방식도 여러가지 인 것 --> dot product 가 그냥 들어갈 수도 있어(w 를 넣을 수도 있고)
			§ 이 vector 에 대해서 weighted sum 만들어내
			§ key와 value 를 구분해서 넣을 수도 있대(근데 이게 보통은 같대) 
			§ Query vector 의 hidden dim output(lstm output) --> 
			§ Lstm 다음에 넣으면 lstm 결과로 나온 것들이 희석될 수 있음
			§ Lstm 전에 넣으면 이전의 결과들을 더욱 존중하는 의미?
			§ Weight 들을 그림으로 표현하면 그래피컬하게 나타낼수도 있어(0이면 까만색, 1이면 흐니색 등)
		○ Attention score function
			§ mlp로 넣거나(non linear로 학습하거나)
			§ Dot product - (이번에 attention all you need 논문에선 이걸로 했어)
			§ Scaled dot product
				□ Dot product 는 Dimension 이 커지면 scale 이 너무 커지더라
				□ 이 스케일 맞추려고 루트 |k|(k 의 dimension)로 나눈 것
	• What do we attend to?
		○ Input sentence
			§ Copy 해서 넣음
			§ Previous word 에 대해서 attention 함
			§ Various modalities - 그냥 grid 쪼개서 그 grid 의 weight 를 그려내면 돼
		○ Hierarchical structures
			§ Word level 의 attention, sentence 단위의 attention 을 따로 구해(sentence 단위는 word 단위에껄 가져다가 쭉 쓰면 됨)
		○ Multiple sources
			§ 여러개 소스에서 얻어서 unknown 인 부분을 채워감
		○ Self attention
			§ 주변을 학습해서 나오는 vector 의 질을 높인다(주변까지 참조해서 뭔갈 내 뱉는다)
			§ (이걸 참조하는게 좋아! 라고 불 들어오는 정도인가봐)…?
	• Improvement
		○ Coverage
			§ 자꾸 반복되는 값을 리턴하는 문제점이 생기기도 함
				□ 하나만 나오게 한다
				□ Embedding 에 이 부분이 이미 커버 됐다 라는걸 표시
		○ Incorporating markov properties
			§ 이전 attention 을 참고하여 다음껄 만들기
		○ Bidirectional training
			§ 양쪽에서
		○ Supervised training
			§ Gold standard 를 놓고 그거에 맞게 학습하도록 함
		○ Alignment 가 아니게 학습되기도 하더라
			§ 그래도 data 가 많으면 이런 현상은 많지 않대
	• Specialized attention varieties
		○ Hard attention
			§ 실수 벡터를 integer vector 로 해버려 --> discrete 해져 --> reinforcement learning 컨셉이 들어가야 학습이 가능해져
		○ Monotonic attention
			§ Alignment 개념상 뒤를 바라볼 필요가 없는 경우가 있어
			§ Speech recognition 의 경우
		○ Convolutional attention
			§ Window 를 활용함
		○ Multi-headed attention
			§ Attention 을 여러개 사용함 / 각각에 서로 다른 역할을 부여함
			§ 명사에만 집중 혹은 괄호에만 집중 하는 등
	• Attention is all you need
		○ Multi-head attention 이 lstm 역할
		○ Residual connection (너무 깊어졌을 때에 더 연결해주는 역할)
		○ Masked --> 답보고 답 맞추기 하면 안돼서 그 부분을 가려놨다는 얘기랭
		○ Encoder 의
			§ 앞에꺼는 q,k,v 가 다 decoder 에서 오고,
			§ 두번째꺼는 q는 de, k,v 는 encoder 에서 와
		○ Encoder 에서 가져오는 부분 
		○ Q, k, v에서의 원본
		○ 1,2번은 self attention / 3 번이 기존에 우리가 썼던 방식
		○ Lstm 이 없어서 속도가 짱 빠르댕
		
		
