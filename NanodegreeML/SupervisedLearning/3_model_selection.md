## model selection
* model complexity graph
	* ![model_complexity_graph](images/3_1.png "model_complexity_graph")
	* Training error 와 testing error 를 각각 graph 로 표현
		* 둘 다 크면 under fit
		* testing error(cross validation error)가 크면 over fit
		* 두개가 비슷하고 작아야해
		* --> 근데 model 선택하는 과정에서 testing data 를 고르는것 자체가 웃기는 일
		* --> training set 안에서 cross validation set 을 두자!

* k-fold cross validation
	* data 재활용
	* 동일한 데이터 안에서 training set 과 validation set 을 shuffle 해서 여러개를 만들어
	* ![K_fold_cross_validation](images/3_2.png "K_fold_cross_validation")
	* Kfold(12,3,shuffle=True)

* Learning curve
	* Under fitting - 높은 지점으로 수렴
	![learning_curve](images/3_3.png "learning_curve")
	* Good - 낮은 지점으로 수렴
	![learning_curve](images/3_4.png "learning_curve")
	* Overfit - 수렴하지 않아
	![learning_curve](images/3_5.png "learning_curve")

* Logistic regression model 을 학습시키는 방법
	* Training set 에서 cross validation set 추려
		* --> degree 각각에 대해서 cross validation set 에서 f1 score 구해
		* --> 이게 가장 좋은 degree 골라
		* --> 이 모델로 testing

* Decision tree
	* --> hyper parameter 설정(depth)
	* --> 각각에 대해서 cross validation set 에서 f1구해
	* --> 가장 좋은 depth 골라
	* --> 이 모델로 testing

* Svm
	* --> hyper parameter(kernal - polynomial or rbf, gamma)
	* --> grid search해
	![svm](images/3_6.png "svm")
	Df.groupby('gender')['age'].mean()
	Df['height'].plot(kind='box') --> show distribution





