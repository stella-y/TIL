Word to vec 이 왜 대용량에 강하게 됐는지!

• Big operations, especially for softmaxes over large vocabularies 
• → Approximate operations or use GPUs 
• GPUs love big operations, but hate doing lots of them 
• → Reduce the number of operations through optimized implementations or batching (for loop 돌리지 말고 matrix 연산으로 해라)
• Our networks are big, our data sets are big 
• → Use parallelism to process many data at once

Sampling -based softmax approximation
		○ 연산양을 줄이는 것(10만 단어 * vec(300)) 뭐 이런거 있을 때에
		○ True label 과 negative sample 몇개를 random sample --> 학습할 때에 연산 량을 줄인다
		○ Softmax 의 분모 부분을 줄인다
	• Importance sampling
		○ sampling이 어려운 대상 함수(p(x)) 대신 다른 함수(sampling 한 q(x)) 사용하여 weight 곱해서 사용
			§ 이때의 Q를 uniform dist ?
	• Noise Contrastive Estimation
		○ 참(positive sampling) 거짓(negative sampling)을 판별하는 문제로 바꾸어 계산
		○ Try to guess whether it is a true sample or one of N random noise samples. Prob. of true: P(d = 1 | xi, hi) = P(xi | hi) P(xi | hi) + N ⇤ Q(xi | hi)
		○ Softmax 한거랑 유사한 결과를 낼 수 있음이 증명돼있음
		○ --> NCE(Noise-Contrastive Estimation)
			§ CBOW와 skip-gram 모델에서 사용하는 비용 계산 알고리즘을 말함. sampling 한 일부 데이터에 대해서만 softmax 함수를 적용.
			§ k 개의 대비되는(contrastive) 단어들을 noise distribution에서 구해서 (몬테카를로) 평균을 구하는 것이 기본적인 알고리즘
			§ 일반적으로 단어 개수가 많을 때 사용, nce를 사용하면 문제를 (실제 분포에서 얻은 샘플)과 (인공적으로 만든 잡음 분포에서 얻은 샘플)을 구별하는 이진 분류 문제로 바꿀 수 있게 된다.
			§ Negative sampling 에서 사용하는 목적 함수는 결과값이 최대화될 수 있는 형태로 구성.
			§ 현재(목표, target, positive) 단어에는 높은 확률을 부여하고 나머지 단어(negative, noise)에는 낮은 확률을 부여해서 가장 큰 값을 만들 수 있는 공식을 사용.
			§ 특히, 계산 비용에서 전체 단어 V를 계산하는 것이 아니라 선택한 k개의 noise 단어들만 계산하면 되기 때문에 효율적.
			§ https://korea7030.github.io/Study13/
		
	• Simple negative sampling
		○ Nc loss 와 비슷하지만 biased estimator
		○ Word2vec 에 많이 쓰임
		○ Similar to NCE, but biased when k != |V| or Q is not uniform
		○ P(d = 1 | xi, hi) = P(xi | hi) P(xi | hi)+N일것
		○ (ppt 가 잘못된걸거야)
	• Mini batching negative sampling
		○ Simple solution : select the same negative samples for each minibatch 



Structure-based softmax approximations

	• Class-based : class 로 먼저 구분 한 다음에 단어를 추론
		○ Predict class first, then word given class
		○ P(c|h)  -> P(x|c,h)  / 계산양이 줄어들지
	• Hierarchical softmax : 
		○ Layer 는 세갠데 weight 는 7개 
	• Binary code prediction


둘의 차이 --> 
Sampling based 는 test 할 때에는 full softmax 연산을 다 해야함
structured 는 weight matrix 자체가 단계별로 존재 --> test time이 줄어들지
