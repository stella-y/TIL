## Exploring Randomly Wired Neural Networks for Image Recognition
https://arxiv.org/abs/1904.01569
* 네트워크 구조를 랜덤하게 자동생성했더니 이미지 인식에 성능이 좋더라
* 본 논문에선 random 그래프 생성 방법을 세개 정도를 써서 비교함
* 이 random 방법론을 더 찾아서 나열하면 더 효과적일거란 idea

### introduction
* skip connection, NAS 에서의 dag 학습 등을 봤을 때 다양한 방식으로 그래프를 그려보는게 도움이 될 것으로 여겨짐
* NAS 연구에서 그래프 생성에서의 한계
	* search space 가 제한적이었음
		* convolution 가능한 쌍이 주어져야, 두개의 쌍이 주어지고 합치는 형식이 되어야함
	* 네트워크 구조 학습할때에 RNN 이용하는데, 이때의 각 rnn cell 에서 뭐가 나와야할 지에 대한 순서가 정해져있음
		* 어떤 cell 에서 뭘 뱉어야 하는지 등(여기서는 relu 를 뱉어내고, 뭐 이런거,,,)
* ==> 본 논문에선 connection 형성에 자유도를 주면 더 좋을 것이라는 아이디어

### related work - network generator
* g: generator runction / theta: patameter / output : Network
1. stochastic Network generator - 네트워크 생성에 
2. ResNet, DenseNet
3. NASNet
	* 모델의 레이어가 모두 연결돼있고, 이 중 최적의 경로를 찾는 최적화 문제로 판단
	* skip 하는 connection 자체를 rnn 통해서 학습함
	* 레이어 형성의 방향성은 사람이 지정하고, 세부 내용만 생성함

### Randomly wired network
* convolution 엔 제한을 두지만, connection 을 넣을 때에 자유도를 넣겠다
* general graph 를 generate 한 다음에, nn 에 쓸 수 있는 형태로 변형하겠다 라는 것(input node, output node 정리 등)
* 테스트한 방법 : ER, BA, WS model
* 그래프 형성 후 네트워크로 바꿀 때에 적용 규칙
	* edge operation : edge 는 dataflow 다.
	* node operation
		* 하나의 노드로 들어오는 모든 인풋은 weighted sum ([0,1] 범위에서)
		* transform : Relu - conv - batch norm 의 형태로 함(익숙한 형태는 conv - batch- relu 일텐데 마지막으로 넘겨주는 값이 weighted sum 이 되니깐 값이 계속 커지는 형태를 막기 위해서)
		* distribution : node 의 output 은 모두 같은 값이 나가게 됨(단순 평균)
	* input, output node
		* 적당히 번호 부여 후에 그 선순위 번호와 후순위 번호에 input node 와 output node 를 넣음 (output 에서는 mean 해서 내 놓을 수 있도록)
* 단계별 출력은 convolution
* 한 step 나갈때마다, 각 step에서의 처음 들어가는 부분은 stride 2 conv 로 사이즈를 줄여나감

### Random graph models
* ER
	* 각 노드들의 연결 여부를 random 하게 결정(random 성을 줘서, 비율 높게 하면, 연결이 많이 되고 하는 식으로 그래프 그려냄)
* Barabasi-albert(BA)
	* hub 가 되는 노드에 더 edge 가 많이 붙도록 generate
	* social network 에 가까운 모델
* WS
	* small world model
	* 규칙적으로 연결 한 다음에, 각 노드별로 시계방향으로 돌아가면서 몇개의 edge 들을 없애고, random 하게 다시 생성하게 될 것
* --> 각 random 생성 방법론 마다 결과 그래프 형태에 차이가 있을 것

### Converting undirected graphs into DAGs
* 생성된 그래프에 순서 부여
	* ER 은 아무렇게나 번호붙임
	* BA 는 새롭게 붙게 되는 순서대로
	* WS 는 시계방향으로 돌아가는 순서
* 순서 흘러가는 방향으로 edge 방향성을 부여하고 나면 그래프가 잘 형성되더라!

### experiment

### analysis experiment
* 3\*3 separable con 가 3\*3 conv, 3\*3 max pool, 3\*3 average 보다 항상 성능이 많이 돟더라
* small size 에서는 나스, 아메바랑 비슷하거나 조금 더 좋고,
* large size 에서는 성능이 많이 낮았음
* 평균적으로는 경쟁력있는 성능을 보였다!






