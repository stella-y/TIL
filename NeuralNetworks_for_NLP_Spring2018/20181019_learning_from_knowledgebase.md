# Learning From/For Knowledge Bases
## Types of Knowledge Bases
	• (Graph db를 염두) 지식 그래프 디자인
	• WordNet(1995)
		○ (part of), (type instance) 등 instance 간의 관계 등을 그래프로 표현 + 수치화 가능하도록
		○ Word2vec 나오기 전까지는 그 못지않은 인기
	• Cyc(1995)
		○ 30년간 세상의 모든 상식을 정리하겠다 라는 일념으로
	• DBPedia(2007)
		○ Extraction of structured data from Wikipedia
	• YAGO (2007)
	• BabelNet(2008)
		○ multi lingual 로 확장
	• Freebase(2008)
	• WikiData(2014)

## Learning Relations from Embeddings
	• 릴레이션 추론
	• Knowledge base 는 태생적인 불완전함이 있어
		○ Can we perform “relation extraction” to extract information for knowledge bases? --> 이런 자동화가 가능해질것인가…?
	• 자동화 시도
		○ Relation Extraction w/ Neural Tensor Networks (Socher et al. 2013)
			§ 
			§ 근데 parameter 가 엄청 커져 (쌍에 대해서 계산하게 되니깐)
		○ Learning Relations from Embeddings (Bordes et al. 2013)
			§ 아래의 loss function 이용
			§ 
			§ 이런식으로 반의어 관계와 동의어 관계를 학습시킴

## Learning from Text Directly
	• Distant Supervision for Relation Extraction (Mintz et al. 2009)
		○ Label 없이 했다고 하네요
		○ Given an entity-relation-entity triple, extract all text that matches this and use it to train
		○ 문장 다 긁어모아서 relation 가져옴(match 형태인 것)
	• Relation Classification w/ Recursive NNs (Socher et al. 2012)
		○ Create a syntax tree and do tree-structured encoding
		○ 양심상 문장 그냥 때려넣지는 않고, parsing tree 구성 후 이를 이용
		○ 
	• Relation Classification w/ CNNs (Zeng et al. 2014)
		○ 에라모르겠다 cnn
		○ 그냥 embeding -> cnn -> fully connected softmax
		○ 

	• Jointly Modeling KB Relations and Text (Toutanova et al. 2015)
		○ To model textual links between words w/ neural net: aggregate over multiple instances of links in dependency tree
		○ 가장 점수 높은 relation pair 를 답으로 줌
		○ 
	• Modeling Distant Supervision Noise in Neural Models (Luo et al. 2017)
		○ 노이즈가 있을거란 가정으로 noise를 모델링에 넣어버림!
		○ Idea: there is noise in distant supervision labels, so we want to model it
		○ 
	
## Learning from Relations Themselves (relation 으로부터 학습)
	• Modeling Word Embeddings vs. Modeling Relations
		○ 만약 잘 됐으면 relation 을 쓰지 embedding 을 쓰지 않았을 수가 있지, 근데 현실적으로 이걸 잘 구성하는게 쉽지가 않앙 @-@
		○ Word2vec 을 넘어서는 정보를 충분히 가질 수 있음
		○ 관계라는 정보가 있으니깐!
		○ (라스는 3대 대통령과 18대 대통령의 예시를 들으셨음…)
	• Tensor Decomposition (Sutskever et al. 2009)
		○ E r e 의 tensor 로 구성해서 연산함
		○ 
	• Modeling Relation Paths (Lao and Cohen 2010)
		○ Multi-step paths can be informative for indicating individual relations 
		○ 단어가 딱 주어지면 어떤 저널로 퍼블리시 해야할지를 찾아준당
		○ 
	• Optimizing Relation Embeddings over Paths (Guu et al. 2015)
		○ Traveling over relations might result in error propagation
		○ Simple idea: optimize so that after traveling along a path, we still get the correct entity 
		○ 
	• Differentiable Logic Rules (Yang et al. 2017)
		○ Relation 1 matrix , relation 2 matrix 의 곱이 and 관계를 나타낸다고 가정해서 디자인
		○ 
		
		○ 

## Using Knowledge Bases to Inform Embeddings
	• Knowledge base 를 이용해서 좀 더 나은 word2vec 을 넣고싶당!
	• Lexicon-aware Learning of Word Embeddings (e.g. Yu and Dredze 2014)
		○ Objective function 이 knowledge 의 정보를 같이 학습하게 디자인
		○ 강아지 <-> 개 일케 있으면 이 둘의 자식 관계를 학습할 수 있도록
	• Retrofitting of Embeddings to Existing Lexicons (Faruqui et al. 2015)
		○ Similar to joint learning, but done through post-hoc transformation of embeddings 
		○ 관계가 붙어있는 것들
		○ Relation 의 방향성이 여러개는 아니다 라는 가정으로 만든 듯
		○ 
		○ 이미 학습되어있는 것과 크게 벗어나면 안된다
	• Multi-sense Embedding w/ Lexicons (Jauhar et al. 2015)
		○ Apple  같은 경우 여러 의미가 있지
		○ 이런 다양한 의미를 relation embedding 은 포함할 수 있으니 word embedding 을 할 때에 이걸 이용해서 쓴당
		○ 
		
