## Highly scalable Deep Learning Training System with Mixed-Precision: Training ImageNet in Four Minutes
1. mixed-precision training method : single machine 에서의 throughput 향상
2. large mini-batch size
3. optimised all-reduce algorithm

### 1. Introduction
- To make full use of the hardware
	- mini-batch size per machine should be properly set and cannot be too small
	- it is common to use large batch to achieve weak scaling (전체적인 throughput을 좋게하고, 모델의 update를 적게 하게 해줌)

- Two challenges when using large batch accross large clusters
	1. larger minibatch size - lead to lower test accuracy
		- large mini batch : reduce the variance of gradients by taking the average of the gradients in mini-batch
		- 근데 이렇게 할 수록 accuracy 가 떨어지는 경향이 있음
	2. large cluster -> communication cost 때문에 머신 갯수가 많아질 수록 near-linear scalability를 달성하기는 어려워진다
		- communication step이 bottle neck 이 되는 경우가 많기 때문에

- Main Contribution
	- T (overall throughput)=S\*N\*e (S: single machine 에서의 throughput / N: # of gpu / e: scaling efficiency)
	- 아래 세가지 전략으로 위의 두개 challenge를 극복함
	1. mixed-precision training with LARS
		- eliminated weight decay on bias and parameters for batch norm and adding proper batch norm layer
	2. Improved S by half-precision training
	3. Improved e by optimizing adative all-reduce collective with ring-based all-reduce in NCCL

### 2. Related work
1. Large-batch training

2. Low-precision training

3. Distributed training on heterogeneous clusters

### 3. System overview
1. Input pipeline module
	- delivers data for the next step before the current step has finished
2. Training module
	- forward/backward computation with mixed-precision and model update with LARS
3. Communication module
	- tensor fusion
	- hybrid all-reduce
	- (optimize the scaling efficiency according to tensor size and cluster size)

### 4. System implementation and optimization
#### 4.1 Mixed-precision training with LARS
- half-precision 을 naive 하게 적용하면 gradient vanish 나 training process가 stall 될 수 있음
- mixed 된 형태로 half-precision 적용
	forward and backward propagation (fp 16)
	-> cast to single precision(fp 32)
	-> LARS (fp 32)
	-> weight update (fp 32)
	-> 32 to 16
	-> forward and backward

#### 4.2 Improvements on model architecture
- 두가지 측면에서 향상시킴
1. eliminated weight decay on the bias and batch norm
2. adding proper batch norm layer for AlexNet


참고 자료
1. All-reduce : https://brunch.co.kr/@chris-song/96
2. LARS : https://www.kakaobrain.com/blog/113
3. Quantization : 
- https://towardsdatascience.com/speeding-up-deep-learning-with-quantization-3fe3538cbb9
- https://post.naver.com/viewer/postView.nhn?volumeNo=19437431&memberNo=20717909
- on tensorflow http://itteckmania.blogspot.com/2018/03/quantize.html











