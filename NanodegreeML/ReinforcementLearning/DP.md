# Dynamic programing
이미 환경에대해서 agent 가 다 알고 있다는 가정

* An iterative method
	* 모든 state 에서의 value를 0이라 가정
	* Current state에서의 value 값을 그 다음 state에서의 값을 이용하여 update(이건 아직까지 결정되어 있을 수없지 —> 첫번째 iteration 에서는 우리가 초기 세팅한대로 0이 들어가버릴거야)
	* 위에서 했던 iteration 을 반복해 (이번엔 다음 state 들이 다 0은 아니겠지) 
	* 이 과정을 반복하면 각 state 의 value가 true value 로 수렴할거야


* Iterative policy evaluation
	* Bellman expectation equation 이용
	* 모든 state  대해서 미리 알고 있는데 어려우니 state value를 지속적으로 update 해감
	* 처음엔 iteration 마다 변화가 크겠지만 어느 순간부터는 적어질 것
		* —> 충분히 작은 값 Theta 를 가정하여 이보다 변화가 작은 순간이 오면 iteration 을 중단하게 함
	* State value 값이 항상 어디론가 수렴한다는 게 증명돼있음…
	• 

