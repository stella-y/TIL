## Deview2019 day1
### Operational AI: 지속적으로 학습하는 anomaly detection 시스템 만들기
https://openreview.net/pdf?id=HkgeGeBYDB
1. 제조업에서 ai 적용이 어려웠던 이유
* 성공사례나 경험 부족으로 인한 리스크가 있음
* 레이블 불균형으로 일반적 분류 알고리즘 적용이 어려움
* 한번의 모델 학습으로는 계속되는 공정 환경 변화에 대응할 수 없음
2. Anomaly detection : RaPP(Reconstruction along Projection Pathway)
* 정상, 비정상 데이터의 분류
	* 비정상 데이터 확보가 어려워, 일반적 분류 모델은 적용이 불가능함
	* 이전의 방법론
		* 차원축소를 통한 특징 추출(pca 등)
		* clustering 통한 확률 분포 근사 (GMM 등)
	* deep learning based method
		* AE based model
			* encoding, decoding 을 통한 특징 추출
			* 차원 축소 기능을 제공함 / 학습이 용이함
			* mse 손실함수 사용으로 복원성능이 떨어짐
		* GAN based methods
			* generator와 discriminator훈련 후에,
fix된 generator에 encoder를 붙임.
			* MSE손실함수에 비해 복원 성능이 향상 됨
			* OriginalGAN은 차원 축소 기능을 제공하지 않음 /학습이 불안정함.
		* **현재 요구사항 상 복원성능은 필요 없으므로 AE 선택**
* AE 에서의 성능향상 꾀하기 - RaPP 방법론
	* (현재 ICRL2020 에 제출된 상태인듯함)
	* encoder 와 decoder 의 중간 결과물을 활용하고자함
	* 원본의 값과 hidden representation 을 비교하는 것 자체는 무의미할 것
	* 그러므로 decoder 에서 나온 값을 다시 encoder 에 넣고, decoder 에서의 이때의 hidden representation 값과 원본을 encoder 에 넣었을때의 hidden representation 의 값을 비교함
	* 각 layer 에서의 정보량 감소 추세가 정상 데이터와 차이를 보이면 이것을 비정상 데이터로 간주하는 것!

