## Representation learning
* Deep network —> 복잡하고 hierarchical 하게 내부적으로 input data 를 표현하게 됨
* Object recognition 같은 task 생각해보면 이런식의 language 가 이해가 될 것
* Unsupervised representation
	* Task driven 의 경우에는 task 의 요구에 의해서 이런 학습이 불필요해짐(object 를 detect 하기 위해서 물리법칙을 표현할 필요는 없을 것)
	* Unsupervised representation 은 좀 더 general한 형태를 보여줘야만 것
* Reading the latent language
	* 주어진 데이터를 좀 더 잘 묘사하는 모델을 필요로 하게 됨(caption 없이 image captioning 을 하는 등)
	* 이게 설명 가능해져야 이 description 들을 이용해 모델을 계획하고 결과를 reasoning 하고 generalise 할 수 있게 될 것
	* 좋은 density model 은 물론 좋은 internal language 를 갖고있지만 역시 blackbox 일 것
* Autoencoder
	http://nolsigan.com/blog/what-is-variational-autoencoder/		
* VAE
	* Loss function 에서 regularizer 가 포함된 negative log-likelyhood
	* Encoder 의 분포(q(z|x))와 p(z)사이의 kl-divergence 
	* q를 써서 p를 표현할 때에 정보가 얼마나 유실되는지를 측정
	* p 는 평균 0 과 분산 1 을 갖는 표준정규분포 p(z) = Normal(0, 1)p(z)=Normal(0,1)
	* Encoder 가 표준정규분포와 다른 z를 output 으로 갖는다면 loss 값에서 손해(penalty)를 본다. 이 regularizer 는 z의 각 숫자를 충분히 다양하도록 만들라는 뜻
* MDL(minimum description length) for VAE
	* Coding cost - Alice 가 본인의 말을 잘 전달하기 위해서 필요로 하게 되는 bit의 수(bits-back coding)
	* Reconstruction cost - bob에게 보내게 될 additional error bits(arithmetic coding)
	* 전달하려는 말 x 를 복원하기 위해 필요한 total message 의 length 는 이 두개의 코스트의 합이될 것
* Code collapse
	* 이상적으로는 vae 는 high-level 의 정보를 code 에 담고, low-level 의 정보를 decoder 가 만들어낼 수 있게 해야함
	* 근데 decoder 가 너무 강력해져버리면, coding distribution 이 p(z|x) 가 아니라 p(z)로 collapse 해버림(decoder가 latent code를 무시하는 현상- posterior collapse)
	* --> bottleneck 통해서 전달되는 정보가 없게 됨 --> latent representation 이 학습되지 않게 됨
	* MDL 관점에서 이 문제 분석 - powerful 한 decoder 는 
		* X 가 독립적으로 전달된다면, 
		* z의 조건 하에 Decoder 에 의해서 저장되는 bit 의 수 = cost of transmitting Z
	* https://dnddnjs.github.io/paper/2018/06/21/vae3/
* Thought experiments
	* Experiment 1 : mnist decoder 가 mixture over 10 disjoint model 을 학습하고 나면, prior 는 10개 class 에 대한 uniform 이 될 것
		* Image class 에 대한 condition 은 log10 bit, encoding class cost log10 이 될 것
	* Experiment 2 : encyclopedia 에서 100개의 character string 을 랜덤하게 선택한다고 가정하자. Paragraph 에서의 context 는 missing 되어있다면, 각 string 에 정보를 append 하는게 의미가 있을 것인가


* Learn the dataset, not the data points
	* 결국 하고 싶은 말은 데이터 점 하나하나를 어떻게 표현할지를 고민하는데 아니고, 전체 데이터를 봤을때에 그 안이 어떻게 조직화 되어있는지를 파악하는 게 중요하다는 것
	* Log-likelihood 로 representation 을 찾을 수는 없을 거야 —> 이건 절대로 high-level information 을 encoding 할 수 없다는 것
		* E.g. sample 자체에는 엄청난 차이가 있더라도 이때의 log-prob 는 되게 작은 차이만을 가지고 있어서…
	* Use high level information to organise low level data, not annotate it
		
* Associative Compression Network
	* VAE 의 loss 를 unconditional prior(p(z)) 에서 conditional prior(p(z|z')로 바꿈
		* (z'는 latent representation of an associated data point)
		* z의 Euclidean 길이로 가장 가까운 k 개의 point
	* p(z|z’) – 모든 것에 대해서 모델링 할 필요 없이, latent space 의 일부에 대해서만 모델링 하게 돼서 coding cost 를 줄여줌
	* 모델이 latent space 의 부분에 불과한 것 - coding cost 가 매우 크게 줄어들더라)
	* Implicit amortisation - code 가 clustered 되는만큼, 모델이 더 가벼워지더라
	* 결과 - decoder 가 powerful 해지더라도 more informative 한 code 가 learn 되더라
	* 그림은 input 이 맨 왼쪽이고, 그 옆에것들이 generate 된 결과 / 이것들을 보면 갖고 있는 high level의 정보가 어떤 내용인지 대충 알 수 있음
		

* Mutual Information
	* 데이터를 최대한 잘 표현한 코드가 필요하더라
	* 수학적으로는 code z 와 data x 간의 mutual information 을 최대화시키고 싶은 것
	* Autoencoder 이거라면 z에서 x 를 decoding 해내는것과 z 없이 decoding 을 해 내는 곳간의 차이가 mi의 lower bound 일 것—> reconstruction cost 를 최소화 하는게 결국 mi 를 최대화 하는 꼴을 것
	* Mi를 최대화 시키는 다른 방법은 없는가
	 
* Contrastive predictive coding
	* Input 으로부터 output 을 그대로 생성한다기보다는, 그 다음에 나올 audio signal 을 예측하는 것에 더 가까움
	* Representation 으로부터 새로운 것을 생성한다기보다는, representation 의 mutual information 을 보다 직접적으로 극대화시키는 방법을 이용함
	* Code 의 descriptiveness 를 최대화시키는 것
