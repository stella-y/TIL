1. svm
	- support vector : 초평면에 가장 가까운 분류기점의 벡터
	- support vector classifier : soft margin 허용(parameter로 오류 허용 정도 결정)
	- support vector machine : 	support vector classifier가 비선형 커널과 결합
		- cost(오차 얼마나 허용할것인지) / gamma(hyperplane이 아닌 kernal과 관련-가우시안 함수의 표준편차를 조정)
2. cross validation	
	- 데이터 크기가 작은경우 validation set을 크게 둘 수 없는데 이게 작으면 test set 에 대한 신뢰성이 낮아짐(모든 데이터가 test에 쓰일 수 있게 함)
3. decision tree
	- 여러 규칙을 순차적으로 적용, 분할하는 분류 모형
	- entropy를 작아지게 하는 방향으로 진행 / 한번 분기할때마다 변수를 두개로 구분, entropy가 감소하는 방향으로 학습 진행
4. random forest
	- decisive 한 column 을 random 하게 선택, 여러개의 decision tree 생성
	- and then vote

## metric
1. confusion matrix
2. f1 score
	- 2\*(precision\*recal)/(precision+recall)
3. auc roc
	- 1-specificity / recall
	- perfect : 1 / good : 0.8 / random : 0.5

## unsupervised learning
1. pca
	- 분산을 최대로 하는 축을 찾아 투영
	- 공분산 matrix의 eigen vector 에서 축소할 크기만큼만 가져옴
2. t-sne₩₩₩₩₩₩₩
	- pca 에서 차원축소 후 변별력 없어지는 군집이 생기는 문제 해결
	- euclid거리를 유사성을 표현하는 조건부 확률로 표현
	- 점하나 선택 -> 이점에서 다른 점까지 거리 측정 -> t분포 이용해 기준점을 t분포상 가운데 위치 시켰을 때 상대점까지 거리에 있는 t분포값을 similarity로 정의 -> similarity를 기준으로 가까운 값끼리 묶어
2. k-means clustering
	- elbow method
	- random k points -> cluster with the closest mean -> new clusteroid
3. hierarchical clustering
	- cluster 간 거리비교 -> cluster 간 최단 거리 중에서 가장 가까운 두개 클러스터 통합

	- 