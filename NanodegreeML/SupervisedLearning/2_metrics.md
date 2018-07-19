## 분류 모델에 쓸 수 있는 metric
* F1 score
	* `2*(precision*recall)/(precision+recall)`
	* Precision 과 recall 을 한번에 나타내기 위해서
		* 두 수의 조화평균을 사용
		* 두 수보다 항상 작게 나온다
* F-beta score
	* (1+b^2)*(precision*recall)/(b^2 * (precision +recall))
	* Precision 이 중요하면 beta 를 작게, recall 이 중요하면 beta 를 크게 설정
	
* ROC curve (Receiver operating characteristic)
	* 1차원 공간에서 두 종류의 점을 가르는 지점으로 Split 
	* 가능한 모든 split 을 생각해서 이 각각의 true positive , false positive rate 을 구함
	* 그리고 이를 plane 에 plot 함
		* 이 plot 한 곳의 넓이
		(perfect split 이면 1(네모), random 은 0.5, good 은 0.8 정도)
	* 얼마나 잘 split 가능한지를 판별 --> 1에 가까울 수록 더 좋은 모델인 것
	* 0.5 이하인 경우 --> flipping 돼 있으면 0일거야

## Regression model 에 쓸 수 있는 metric
* Mean absolute error --> 절대값은 미분이 불가능해서 gradient decent 등에서는 쓸 수가 없음
* Mean squared error --> error 를 제곱
* R2 score --> simplest possible model 과 비교해서 얼마나 다른가
	* Simplest possible model : 모든 점들을 평균내서 그은 선
	* R2=1-(mse/simplest model 의 평균선)
		--> 이게 크면 좋은 모델 / 작으면 안좋은 모델
