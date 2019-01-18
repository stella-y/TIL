## Distrubuted Representations of Sentences and Documentation(Doc2vec)
* https://arxiv.org/abs/1405.4053
* 개요
	* 기본적 idea 는 word2vec 과 완벽히 같음
		* skip gram - 현재 단어로 주변 단어를 예측하는 방식
		* cbow - 주변 단어로 현재 단어를 예측하는 방식
	* 문장 embedding에 같은 방식을 활용하는 것
	* embedding 을 통한 classification 등의 성능을 높일 것을 기대하는 것
* 대상 paragraph 에 id 를 부여해서, 추가한 것
* 문서 = paragraph * length
* paragraph 를 추가해놓고, word2vec 과 같은 구조로 예측 모델을 돌리는 것
* doc2vec 은 멘탈도 터지고 메모리도 터진다... --> word2vec 은 word size 라도 조절하지만 이건 그런 scaling 을 하는게 쉽지 않기 때문에
(10만 내외인 경우엔 쉽게 시도할 수 있으나 그 이상이면 고려가 필요함)
* pv-dm - cbow와 대응(얘가 더 성능 좋더라)
* pv-dbow - word2vec 의 skip gram 에 대응
	* paragraph id 로 이를 구성하는 word 들을 예측
* pv-dm, pv-dbow 의 값의 sum 보다는 concat 하는게 성능이 더 좋더라