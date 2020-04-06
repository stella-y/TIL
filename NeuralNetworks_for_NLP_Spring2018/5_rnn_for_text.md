## RNN 이용한 nlp
* nlp --> word, character, sentence 관점에서 sequence data 로 볼 수 있음
![rnn](images/5_1.png "rnn")
![rnn2](images/5_2.png "rnn2")
* rnn training - unrolled graph is a well-formed (DAG) computation graph
* rnn 으로 하면 --
	* 문장 전체를 읽고 prediction 하는게 가능해짐
	* 문장 내 context표현 가능
	* 활용 - tagging / language model(각 태그가 next word 인 tagging job 으로 볼 수 있음) / calculating representations for parsing
* 이때의 응용 --> 보통 bi-rnn
	![bi-rnn](images/5_3.png "bi-rnn")
	* 정방향과 역방향을 동시에 학습한다
	* 앞에 있는 input 들은 희석될 수 있으므로, 정방향과 역 방향을 다 쓰게 되는 구조
	* Out1 과 out 5(prediction)을 concat 하는 방식
	* 그냥 하는거에 비하면 언제나 성능 향상이 있어

### RNN으로 할때의 문제점과 그 해결
1. vanishing gradient
	![vanishing gradient](images/5_4.png "vanishing gradient")
	* 다시 미분 또 미분 또미분 하는 과정을 거치면서 앞서 들어온 input 에 대한 gradient 값은 점차 소멸될 수 밖에 없음
1.2 solutions
	* LSTM(Long Short-term Memory)
	(Hochreiter and Schmidhuber 1997)
		* time step 간 additive 한 connection 을 만들어가
		* 곱셈아닌 덧셈 이용해서 gradient 가 사라지는걸 방지
		![LSTM](images/5_5.png "LSTM")
			* C_t : 냉장고라 표현 / 전달되는 것들을 c로 따로 빼놔
			* I --> gate (sigmoid) -~100% 사이에서 냉장고에 몇퍼센트나 넣어 놓을 것인가
			* O --> output 에 얼마나 많이 넣을 것인가
	* 이외에도 여러 대안이 있당
		* Lots of variants of LSTMs (Hochreiter and Schmidhuber, 1997)
		* Gated recurrent units (GRUs; Cho et al., 2014)
		* All follow the basic paradigm of "take input, update state"
2. Efficiency/Memory tricks
* Handling mini-batching
	* minibatch 를 하는게 훨씬 빠르지만 feed-forward network 에서 하는것과 비교하면 rnn 에서 이걸 하는게 훨씬 어렵다
		* 각 단어들이 이전단어에 종속적이고 / sequence 의 길이가 다 다르니...
	* 길이가 다른 문제점에 해결법! --> padding
		* 단 이때에 얘들은 backprop 하지 않겠다는 표시 해 두어야한다(masking)
		![minibatch_with_padding](images/5_6.png "minibatch_with_padding")
	* 해결법 2!!
		* padding 너무 많이하면 성능이 될 수 있다 (batch 하나에 빈칸만 잔뜩들어가게 될 수 있기때문에...)
		* Bucketing/sorting
			* 길이가 비슷한 sentence 끼리 같은 batch 로 돌아가게해서 성능이 향상될 수 있을 것
			* Sentence 길이가 비슷해서 공간 낭비가 크지 않게 될것이당
* Handling long sequences
	* 긴 문장에서 long-term dependency 를 capture 하고 싶어질 경우가 있음
	* 근데 이게 메모리에 맞지 않는다면...
	* 해결법! --> Truncated BPTT
		* BackPropagation Through Time
		* State 는 그대로 가는데 backpropagation 은 처음부터 끝까지 다 하는게 아니고 중간에까지만 해버리는 것
		![Truncated_BPTT](images/5_7.png "Truncated_BPTT")

### Pre-training/Transfer learning for rnn
* rnn 이 성능은 좋은데 데이터가 많이 필요하고, 오래걸림
* 하나의 task 에 대해서 train 한다음에 다른 문제를 풀게해
* pre-training task 는 학습이 쉽고 데이터 양이 많은 task / main task 는 학습이 어렵고 데이터가 적은 task
	* Language Model --> sentence classifier

### gradient clipping
- why?
	- rnn은 bptt 통해서 시간에 역행하면서 기울기를 구하는데, 매 time-step마다 rnn의 파라미터에 기울기가 더해져서 출력의 길이에 따라서 기울기 크기가 달라짐
	- 학습률을 조절해서 gradient descent update 속도를 조절해야 함
- gradient clipping
	- 신경망 파라미터 $\theta$ 의 norm(보통 L2 norm)을 구하고, 이 norm의 크기를 제한
	- 기울기 벡터gradient vector의 방향은 유지하되, 그 크기는 학습이 망가지지 않을 정도로 줄어들 수 있음
	- 물론 norm의 최댓값을 사용자가 지정해주어야 하므로 또 하나의 하이퍼파라미터가 생기지만, 최댓값보다 큰 norm을 가진 기울기 벡터의 경우에만 그래디언트 클리핑을 수행하므로, 능동적으로 학습률을 조절하는 것과 비슷한 효과를 가질 수 있음

https://kh-kim.gitbook.io/natural-language-processing-with-pytorch/00-cover-6/05-gradient-clipping
