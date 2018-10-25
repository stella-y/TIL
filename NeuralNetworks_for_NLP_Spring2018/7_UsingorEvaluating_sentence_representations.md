## sentence representation
* vector 로 나타낼 수 있음
* 활용
	* sentence classification / paraphrase identification / semantic similarity / entailment / retrieval

### Sentence Classification
* tolic, sentiment, subjectivity/objectivity 등등 여러가지로 분류해둬

#### Paraphrase Identification(동일한 문장 알아채기)
* 데이터 예시
	* Microsoft Research Paraphrase Corpus (Dolan and Brockett 2005) --> 5800 sentences (질은 좋은데 양이 적엉)
* 모델 - sentence 를 vector 로 나타내고 이 둘사이의 similarity 를 계산하는 classifier로 돌려
	1. Skip-thought Vectors (Kiros et al. 2015)
		* general method
		* unsupervised training : large scale data로 주변 문장들 학습 (Using encoder-decoder)
