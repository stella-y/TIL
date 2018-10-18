## Unsupervised and Semi-supervised Learning of Structure
* Unsupervised , semi-supervised 로 parsing tree, dependency tree 등을 learning 하는 것
* Semi-supervised learning
	* X, y 같이 있는 것도 있고, x 만 있는 것도 있고…
* Feature 를 learning 하는 것과 structure 를 learning 하는 것의 차이
* Classifier 에 structure 를 붙여서 쓰는 등으로 활용할 수 있겠지
* Unsupervised feature learning
	* Cbow (word2vec)
	* Skip-gram (word2vec)
	* Sentence-level auto-encoder
	* Skip-thought vectors
	* Variational auto-encoder
* Objective
* Clustering words in context
	* Train word embedding / k-means 써버리는 것
	* 명사이면서도 동사인 것들 이런것들에는 대응이 되지 않는 편
* HMM
	* Label 이 주어져 있는 경우 / 
	* EM style 의 학습
		* 근데 몇번째에 봉우리가 생길지 아무도 알 수가 없어 그래서 번호를 매겨놓고, 이 번호가 명사구나 이 번호가 동사구나 라는걸 알 수 있도록
	* 최신의 방법 --> 답을 discrete 하게 내는게 아니고, word embedding 과 같은 뭔가 분포를 내 놓게 할 수 있어
	* Lstm 을 바로 적용하지는 않고, state 를 discrete 하게 남겨둬(lstm 의 디자인을 transition matrix 를 내는 데에 까지만으로 활용하는 것)
* Conditional Random Field Autoencoder
* Unsupervised Phrase-structured Composition Functions
	* Tree structure 학습
		* Soft(모든게 연결 돼 있는 대신 연결된 정도가 쓰여지는 그런 개념) vs hard
* Weakly supervised : given x and v to model p(y|x) / 
* Gated convolution
	* Machine translation 에 이용
* Learning with RL
	* rl로서 tree structure 를 구성한 다음 이를 다시 classifier 에 넣는 등
* Learning with layer-wise reduction
	* 합치고 점수 높은걸 합치고, 합치고 하는 식
* Learning dependencies
	* 언어적인 dependencies 를 학습
		* 단어의 의미적인 의존관계
* Language 자체에 대해서 feature learning 시도
		
