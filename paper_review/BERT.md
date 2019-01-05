## Bert
* Semi-supervised model
  * (Pre-training) 대형 코퍼스에서 unsupervised learning으로 general-purpose language understanding 모델 구축
  * (Fine-tune by supervised learning) supervised learning으로 QA, STS 등 하위 nlp 테스트에 적용함
* 모델
  * Input embedding
    * Position embedding을 사용 / 여기에 segment embedding을 추가
      * Position embedding - 각 토큰의 위치 정보(위치에 따라 차례되로 값이 부여되는 range(0, max_len)의 값)의 embedding
      * Segment embedding - 입력 문장의 종류에 따라 다르게 입력되는 값(seg가 token type)
    * 세계의 임베딩 합산 결과를 취하게 됨
      * Position embedding + segment embedding + token embedding
      * i.e. embedding=tok_emb(x)+pos_emb(pos)+seg_emb(seg)
  * Encoder block
    * Base model은 12개, large model은 24개로 구성
    * 입력 시퀀스 전체의 의미를 N번 만큼 반복적으로 구축하는걸 의미 —> 블럭 수가 많을수록 단어장에 보다 복잡한 관계 포착 가능할 것
		* Rnn과 유사하게 병렬처럼 아니라 전체가 recursive하게 반복 처리되는 형태
    * 블럭 내 입력 처리 결과는 매번 residual connection으로 처리 (non-linear activation 거치지 않고 network직접 흐르게 하여 explod, vanishing gradient 문제를 최소화)
