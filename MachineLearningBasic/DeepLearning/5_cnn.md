### Pooling layer
* Second and final type of layer
* cnn layer 에서 dimension 이 많아지면 parameter 가 많아질 수밖에 없음 --> overfit 될 가능성이 높아질 수밖에 없다.
* pooling layer 를 두어서 dimension 을 줄여버림
* Max pooling layer
	* 현재 window 에서 가장 큰 수를 추출해서 다음으로 넘긴다
* Global average pooling layer
	* 전체 image 에서 globalAverage value 가져간다
	* 각 depth 에서 하나의 값들만 남을것.
