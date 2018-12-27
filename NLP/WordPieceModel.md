## Word Piece Model
* tokenizing problem
* 단어를 finite subword unit 으로 표현
* 언어에 상관 없이 모두 적용 가능 / 적용할 언어마다 해당 언어 특징을 반영한 토크나이저를 만들지 않아도 됨


### word piece, units of words
* 단어 갯수 만큼 embedding vector 를 학습함 --> 단어 갯수가 많을 수록 차원이 크거나 모델이 무거워짐 --> 제한된 갯수의 단어만 사용함
* 자주 이용되지 않는 단어(long-tail)은 무시됨
* --> 토크나이징 방법에 따라 모호성이 적은 최소한의 유닛을 만들 수 있음
	e.g.
	```
	공연은 끝났어 -> ['공연-' + '-은' + '끝-' + '-났어']
	공연을 끝냈어 -> ['공연-' + '-을' + '끝-' + '-냈어']
	개막을 해냈어 -> ['개막-' + '-을' + '해-' + '-냈어']
	```
* --> 이런식으로 하려면 언어학적 지식, 학습데이터가 필요해짐
* --> Word piece model(sentence piece) tokenizer
	*  Heuristic 이용한 것 --> 빈도수를 이용하여 어떤 unit으로 나눌지를 결정
1. 한 글자 단위로 모두 띄어 초기화(character 는 기본 subword unit인 것)
2. loop 돌면서 빈도수 가장 많은 bigram 찾기
3. bigram 을 하나의 unit 으로 merge
- 2~3의 과정을 num_merges 만큼 반복


### BPE(Byte-pair Encoding)
* Neural Machine Translation of Rare Words with Subword Units (Sennrich et al., 2015)
* Byte pair encoding --> 데이터 압축 방법
	* 빈도수가 많은 최장 길이의 substring 을 하나의 unit 으로 만들면 bit 를 아낄 수 있음
	* 자주 이용하는 단어는 그 자체가 unit 이 되며, 자주 등장하지 않는 단어는 subword unit 으로 나뉘어짐
* BytePairEncoder(n_units)은 n_units 개수만큼 subword unit 학습


### 

https://lovit.github.io/nlp/2018/04/02/wpm/