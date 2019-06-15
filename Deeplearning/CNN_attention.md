## CNN attention-based networks
* NLP 뿐 아니라 이미지에서도 attention 을 적용해봤을때의 효과가 어땠는지 설명
* Attention
  * 쿼리, 키, 밸류 
		○ 쿼리 - 각 밸류 중에서 어느정도를 가져오고 싶은데, 얼만큼가져오면 될까? 라는 질문같이 것- 각 밸류들을 얼마나 가져가면 좋을지를 output 으로 내게 될 것
		○ Q*W*K 이  를 학습시켜서 쓸 수 있는 것
		○ 어떤 칸에 대한 값이 진화해나가는데, 나만 보는데 아니라 주변의 값을 참고해서 가져가게 되는 것, 이때에 얼마나 가져갈 것인지는 나타내는 vector 를 가져가게 되는 것
		○ Fully connected Neural network
			§ W를 얼만큼 가져가지는 생각하지 않고 전체를 동일한 비율로 가져가게 되는 것
		○ CNN
			§ 한정된 양 만큼을다음의 output 을 나는데요 활용하게 되는 것
			§ 혀내의 위치가 제약사항으로 들어가게 되는 것
		○ Attention
			§ Input의 중요도 만큼(weight)으로 주변의 정보를 활용하겠다(input 에 따라 변화하는 weight를 갖고 가겠다 라는 것)
			§ W_n=softmax(f(BS, K_n)) - BS : 현재의 상태, k_n : 모든 키의 값, w_n: n에서의 weight
