## Combating label noise in deep learning using absteintion
* label noise 해결이 주 목적 - label 에 noise 가 끼는걸 abstentioning 으로 극복하자 뭐 이런거
* large scale labeling
	1. annotation platform 이용(Amazon mechanical Turk - 인도...)
	2. automatic collections of web-based data using meta-information(hash tag 수준일 것/검색 결과를 쓰는 등...)

### steps
1. 기권을 위한 class 를 하나 더 만들어둠(class k 개 +1)
2. k+1번째 class 로 분류된거 빼버림
3. 다시학습

### abstention 수 조절
* trade off - 많으면 정보가 없어지고, 적으면 noise 가 많아지고

### loss function
* 기본 cross entropy term 에서 (1-abstention class probability)로 나누고, 여기에 cross entropy term 을 abstention class probability 가 높을 수록 무시하게 한다
* + 여기에 abstraction probability 가 높을수록 loss 값 또한 커지게 디자인
* remarks
	* --> 항상 true label 에 대해서는 정상적으로 학습이 된다.
	* The gradient of loss w.r.t abstention class is determined by abstention penalty, alpha
* --> alpha 조절 algorithm
	* epoch L 만큼은 abstein loss 를 사용하지 않음 / 
	(점점 alpha 값이 강해지는 design)
https://arxiv.org/pdf/1905.10964.pdf


