## Deview2019 day1
### Operational AI: 지속적으로 학습하는 anomaly detection 시스템 만들기
> 요약.
> 1. anomaly detection
> 	- auto encoder 이용함
> 	- hidden layer 에서의 결과도 score 에 이용하기 위해서 Rapp 방법론(https://openreview.net/pdf?id=HkgeGeBYDB) 사용
> 	- (decode 결과를 다시 모델에 넣어서, 원데이터 넣었을때와의 차이 값을 이용 / 이 값의 정상데이터와 비정상데이터간 차이를 score화한다)
> 2. 지속적 모델관리
> 	- model archiving

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
				* generator와 discriminator훈련 후에, fix된 generator에 encoder를 붙임.
				* MSE손실함수에 비해 복원 성능이 향상 됨
				* OriginalGAN은 차원 축소 기능을 제공하지 않음 /학습이 불안정함.
			* **현재 요구사항 상 복원성능은 필요 없으므로 AE 선택**
	* AE 에서의 성능향상 꾀하기 - RaPP 방법론
		* (현재 ICRL2020 에 제출된 상태인듯함)
		* encoder 와 decoder 의 중간 결과물을 활용하고자함
		* 원본의 값과 hidden representation 을 비교하는 것 자체는 무의미할 것
		* 그러므로 decoder 에서 나온 값을 다시 encoder 에 넣고, decoder 에서의 이때의 hidden representation 값과 원본을 encoder 에 넣었을때의 hidden representation 의 값을 비교함
		* 각 layer 에서의 representation 형태가 정상 데이터와 차이를 보이면 이것을 비정상 데이터로 간주하는 것!
		* Normalized aggregation: layer 별 hidden reconstruction error의 분포들을 하나의 차원으로 본 multivariate gaussian이라고 했을 때, SVD를 통해 정규화된 unit-gaussian의 형태로 바꾸어 원점으로부터의 거리를 anomalyscore로 활용
	* score 의 평가 : auroc 통해서 정상, 비정상 분포 분리정도를 측정한다.
3. 지속적 관리
```
비효율적 레이블링 - active learning
catastrophic forgetting - continual learning (incremental training / inclusive training)
테스트 데이터 없는 문제 - sanity check
실행 주체 일원화 불가 - auto-report, auto-integration
```
	* 전체 데이터에대한 재학습 없이 새로운 데이터에 대처 - 여기서는 model archiving 으로 해결함
		* 정상 데이터 학습한 모델을 아카이빙 해둠
		* 이 중 1개의 inference 만 정상데이터라도 정상데이터로 판정
		* 성능향상
			* 이떄 sample 모델이 속할 가능성 예측해서 불필요한 추론과정 최소화
			* 비슷한 분포를 위한 모델들은 재학습 시켜서 통합시킴

### 레이블링 조금 잘못돼도 괜찮아요: Clova가 레이블 노이즈 잡는 법
> 요약
> automl 로 데이터셋 품질 개선 : PICO(Probabilistic Iterative Correction) 알고리즘

레이블 노이즈 해결법
1. robust 한 model 쓰기 --> 무거운 모델은 서빙+훈련 계산량이 매우 큼
2. curriculumn learning / mentor net --> 추가 데이터가 더 필요해짐
3. data cleaning - 수작업 or active learning --> 결국은 수작업...
* split - train - check 방법

* MultiSplit - Train - Check - Vote 방법
	* split-train-check
		* correction 용도로 훈련한 model 이용해서 label 수정
			* label data 를 training set 과 validation set 으로 분리한 후 training data 로 모델을 학습시킨다. / 그 모델로 validation set 을 inference 했을때에 label 되어있던 결과와 그 값이 다르면 모델을 믿고 label 을 update 한다.
		* 근데 이러면 모든 데이터를 검사할 수는 없음
	* multisplit - train - check - vote
		* 여러 버전의 split branch 를 구성(multisplit) / label update 를 위해 각 branch 의 split-train-check 결과를 결합(vote)
		* voting 방법!
			1. 가장 단순하게는 majority vote
			2. PICO(Probabilistic Iterative COrrelation)
				- checker 의 결과가 soft value 인걸 이용하고자(majority vote 와는 달리)





