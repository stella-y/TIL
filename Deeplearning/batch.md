- batch : 전제 dataset에 대한 error 구한 후 기울기 한번만 계산해서 parameter update
	- 에러값을 전체 data 에 대한 loss function 의 (합으로 정의 or 평균으로 정의)해서 w 에 대한 편미분 수행
	- 장점
		1. 전체 데이터에 대한 update가 1번 이뤄져서 update 횟수가 적다(전체 계산 횟수가 적다)
		2. 전체 data 에 대해 error gradient 계산하게 되니 optimal로 수렴이 안정적이다
		3. 병렬처리에 유리함
	- 단점
		1. 한스텝에 모든 학습셋 사용 : 시간이 오래걸림
		2. 전체 학습 데이터에 대한 error를 모델 update때까지 축적해야해서 메모리 사용 +
		3. local optimal에서 나오기가 힘듦
- sgd : 추출된 데이터 1개에 대해 error gradient 계산 / gradient descent 알고리즘 적용
	- 모델 레이어 층 : 1개의 행렬 곱 여러개 묶음 데이터는 행렬. 즉, 여러 묶음 데이터를 특정 레이어에 입력 = 행렬\*행렬
	- sgd는 입력데이터 1개만 사용 -> 벡터\*행렬 계산
	- 장점
		1. shooting 발생으로 local optimal 에 빠질 리스크가 적어짐
		2. step 에 걸리는 시간이 짧아서 수렴 속도가 상대적으로 빠르다
	- 단점
		1. global optimal 찾지 못할 수 있음
		2. 1개씩 처리하므로 gpu성능을 전부 활용할 수 없음
- msgd
	- 데이터셋에서 m개 뽑아 각 데이터에 대한 기울기 m개 구하고, 그 평균 기울기로 모델 update
	- 1000개 데이터 batch size 10 이면 100개 mini batch
		-> 100개 iteration이 1개 epoch
	- 장점
		1. BGD 보다 local minimal 에 빠질 리스크가 적다
		2. SGD보다 병렬 처리에 유리하다
		3. 메모리 사용이 BGD보다 적다
	- 단점
		1. batch size설정해야함(2의 제곱수 많이 쓰는데, 많은 벡터계산이 2의 제곱수가 입력될때에 빠르기 때문)
		2. error정보를 minibatch만큼 축적하므로 SGD보다 메모리 사용 +
		

