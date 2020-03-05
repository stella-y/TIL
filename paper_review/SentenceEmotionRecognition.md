##1. CNN+LSTM Architecture for Speech Emotion Recognition with Data Augmentation
1. 개요
	- SER 데이터 다룰때에 두가지 방법
		1. hand-crafted acoustic feature 제작 해서 neural net 에 넣는 방법
			- e.g. MFCC, pitch, energy, ZCR...
		2. preprocessing 이후에 바로 neural net에 넣기
			- preprocessing e.g. Fourier transform
	- 이 논문에서는 두번째 방법 사용
2. Data augmentation
- Vocal Track Length Peturbation(VTLP)사용 
	- 사람의 성대 길이는 rescaling the peaks of significant formants along the frequency axis with a factor α taking values in the approximate range (0.9, 1.1) 로 모델링 됨
	- 이 점을 그대로 활용해서 original spectogram을 frequency 축으로 rescaling 하면 된다!
- 이 논문에서는 두가지 방향으로 augumentation 실험 수행
	1. single uniformly distributed alpha in (0.9, 1.1) 로 매 epoch마다 모든 training set에 적용했고, validation 에서만 원래 데이터 사용
	2. alpha 적용을 training 뿐만 아니라 validation set에도 사용
