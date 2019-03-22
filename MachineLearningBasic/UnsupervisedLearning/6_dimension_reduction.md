## Dimension reduction
* curse of dimensionality : 관측 데이터의 벡터 공간은 엄청 큰데 필요한 true data 는 작은 차원 공간으로 표현해도 충분한 경우
* 차원 줄이는 두가지 방법 : feature selection vs feature extraction
	* feature selection(변수 선택)
		* 변수 중에서 중요한 몇개만 고르고 나머지는 버리는 방법
		* 변수간 **중첩이 있는지**, 어떤 변수가 중요한 변수인지, 어떤 변수가 **타겟에 영향을 크게 주는 변수**인지를 분석할 필요가 있음
		* 대표성이 가장 큰 주요필드 몇개만 선택하여 대표 feature 로 활용
		* 중첩되는 변수 찾기 - 상관 분석
			- 상관 계수가 높거나 VIF(분산 팽창지수)가 높은 중첩 되는 변수들 중 하나만 선택
		* 타겟에 큰 영향을 주는 중요 변수 찾기 - 랜덤포레스트
	* feature extraction
		* 모든 변수들을 잘 조합해서 데이터를 잘 표현할 수 있게 하는 새로운 변수를 만들어냄
		* e.g. pca

### pca
* 여러 변수가 있는 데이터 차원에서 가장 주요한 성분을 순서대로 추출하는 기법
* 여러 변수의 값을 합쳐서 그보다 적은 수의 주요 성분을 새로운 변수로 하여 데이터를 표현
* 주성분 --> 그 방향으로 데이터들의 분산이 가장 큰 방향 벡터
* pca : 입력 데이터들의 공분산 행렬에 대한 고유값 분해
	* 이 때 나오는 고유벡터가 주성분 벡터
	* 고유벡터가 주성분 벡터 - 데이터의 분포에서 분산이 가장 큰 방향
	* 고유값 - 그 분산의 크기
![pca](image/6_1.png "pca")
* 참고
https://wikidocs.net/7646
https://bcho.tistory.com/1209
http://mllab.sogang.ac.kr/index.php?mid=research_subj_fs
https://kkokkilkon.tistory.com/127
https://darkpgmr.tistory.com/110
