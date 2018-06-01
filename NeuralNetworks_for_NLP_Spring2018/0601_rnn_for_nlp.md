# RNN 을 이용한 nlp
	• Bi-rnn
		○ Bidirectional rnn
			§ 정방향과 역방향을 동시에 하겠다
			§ 앞에 있는 input 들은 희석될 수 있으므로, 정방향과 역 방향을 다 써
			§ Out1 과 out 5(prediction)을 concat 하는 방식
			§ 그냥 하는거에 비하면 언제나 성능 향상이 있어
	• Vanishing gradient
		○ 해결법 1 - lstm
			§ 곱셈아닌 덧셈 이용해서 gradient 가 사라지는걸 방지
			§ C_t : 냉장고라 표현 / 전달되는 것들을 c로 따로 빼놔
			§ I --> gate (sigmoid) -~100% 사이에서 냉장고에 몇퍼센트나 넣어 놓을 것인가
			§ O --> output 에 얼마나 많이 넣을 것인가
	• Handling mini-batching
		○ 이걸 하는게 훨씬 빠른데 rnn 에서는 쉽지가 않아
			§ 이전 단어에 종속적이므로 / 길이가 다 다르기때문에…
			§ 길이문제
				□ Padding 으로 해결 --> 단 이때에 얘들은 backprop 하지 않겠다는 표시 해 두어야(masking)
	• Bucketing/sorting
		○ 비슷한 것끼리 묶으면 성능이 더 좋아
			§ Sentence 길이가 비슷해야 공간 낭비가 없겠지
	• Handling long sequences
		○ Truncated BPTT
			§ State 는 그대로 가는데 backpropagation 은 처음부터 끝까지 다 하는게 아니고 중간에까지만 해버려
			§ 병렬화 하려면
	• Default
		○ 이미 이 자체가 많은 input 을 받을 수 있는 상태야 그래서 이 이전에 input 으로 들어가는 word 들을 word to vec 을 먼저할 필요가 없기도 하징
		○ embedding 하는게 학습하는 과정(이 이전에 word to vec을 추가할 수 있는 것)




	• BPTT - BackPropagation Through Time
	• The unrolled graph is a well-formed(DAG)
	• Computation graph- we can run backprop
	• Parameters are tied across time, derivatives are aggregated across all time steps
		○ (parameter 들이 시간에 종속적 / 미분값들이 모든 time step 에서 aggregated 된다)
		○ Parameter 들이 정도에 따라서 다르겠지만 
	
	


	• Rank -linear algebra 에서의 rank https://en.wikipedia.org/wiki/Rank_(linear_algebra)
	• Breaking the Softmax Bottleneck: A High-Rank RNN Language Model (ICLR 2018 Oral)
	• Rank 가 밚이 필요할 때에는 분명히 효과가 있는 논문(language model 등)
	• Soft max 만으로 하기에는 너무나 많은걸 생략하게 된다(rank 의 값으로 upper bound 가 정해져버리게 됨)
	• 그래서 이걸 해결 하려고 soft max 여러개를 써서 학습해서 사용하게 됨