## Conditioned language model
* Language model 이 text 에 대한 generative model 이라면 Conditioned language model 은 특정 조건혹은 context에 대한 generative model 이라고 볼 수 있음
![CLM](images/8_1.png "CLM")
* 동일한 input 이지만 원하는 결과가 translate 일수도, 다음 문장의 예측일 수도 있으니깐(?)

### Formulation and modeling
* Sentence 에 대한 probability 를 계산하는게 기존의 language model 이라면 여기에 Context term 을 추가한 것
![LM](images/8_2.png "LM")
![clm](images/8_3.png "clm")
	* (선행 문장 뿐 아니라 context 를 따로 또 삽입)
* 차이
	* 보통의 language model 은 lstm 을 씀
	![lstm_lm](images/8_4.png "lstm_lm")
	* Conditioned language model 에서는 context 를 decoder 의 첫번째 값으로 넘긴다
	![lstm_clm](images/8_5.png "lstm_clm")
* hidden state 를 어떻게 전달할 것인가
	* decoder 를 encoder 로 시작하도록 하거나
	* encoder 에서 나온걸 transform 해서 전달하거나(dimension 이 다른 경우)
	* 모든 time step 에서의 input 으로 전달하거나
	![hidden_state](images/8_6.png "hidden_state")


