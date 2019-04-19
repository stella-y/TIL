## Exploring Randomly Wired Neural Networks for Image Recognition
* 랜덤하게 그렸더니 학습이 잘 되더라(이미지에서)
* random 에 대한 방법을 세개 정도를 써서 비교함
* 이 random 방법론을 더 찾아서 나열하면 더 효과적일거란 idea

### introduction
* skip connection, NAS 에서의 dag 학습 등을 봤을 때 다양한 방식으로 그래프를 그려보는게 도움이 될 것으로 여겨짐
* NAS
	* search space 가 제한적이었음 - convolution 가능한 쌍이 주어져야, 두개의 쌍이 주어지고 합치는 형식이 되어야함
	* 학습은 rnn 으로 함 --> 이때의 각 rnn cell 에서 뭐가 나와야할 지에 대한 순서가 정해져있음(여기서는 relu 를 뱉어내고, 뭐 이런거,,,)
	* ==> connection 에 자유도를 주면 더 좋을 것이라는 아이디어

### main topic
* network generator 를 만들어보자 --> random 하게
	* 일단 세가지 random 방법론을 내 놓았고, 이것들을 학습해보면 어떤게 더 나은 선택인지 알 수 있을 것

### related work
* NAS - 최적화 문제로 풀었었고, 그래서 강화학습으로 풀려는 시도가 있었음
* search space 는 제한적이라 이렇게 접근된거였고, 이 제한을 가급적 풀고, 학습하고자 함(connection 에 한해서는 완벽히 자유롭도록)

#### network generator
* g: generator runction / theta: patameter / output : Network
1. stochastic Network generator - 
2. NAS : 

### Randomly wired network
* convolution 엔 제한을 두지만, connection 을 넣을 때에 자유도를 넣겠다
* 테스트한 방법 : ER, BA, WS model
* general graph 를 generate 한 다음에, nn 에 쓸 수 있는 형태로 변형하겠다 라는 것

* edge operation : data flow
* node operation
	* 하나의 노드로 들어오는 모든 인풋은 weighted sum
	* transform : Relu - conv - batch norm 의 형태로 함(익숙한 형태는 conv - batch- relu 일텐데 마지막으로 넘겨주는 값이 weighted sum 이 되니깐 값이 계속 커지는 형태를 막기 위해서)
	* distribution : node 의 output 은 모두 같은 값이 나가게 됨

* input, output node
	* 적당히 번호 부여 후에 그 선순위 번호와 후순위 번호에 input node 와 output node 를 넣음 (output 에서는 mean 해서 내 놓을 수 있도록)

* 각 step에서의 처음 들어가는 부분은 stride 2 conv 로 사이즈를 줄여나감

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
* ER 은 아무렇게나 번호붙임
* BA 는 새롭게 붙게 되는 순서대로
* WS 는 시계방향으로 돌아가는 순서
* 순서 흘러가는 방향으로 edge 방향성을 부여하고 나면 그래프가 잘 형성되더라!

### experiment
* 

### analysis experiment
* 3\*3 separable con 가 3\*3 conv, 3\*3 max pool, 3\*3 average 보다 항상 성능이 많이 돟더라

실험해보니, 
resnet 보다는 성능이 조금 좋았다
obj detectionn - 성능 좀 안좋음


small size 에서는 나스, 아메바랑 비슷하거나 조금 더 좋고,
large size 에서는 성능이 많이 낮았음

평균적으로는 경쟁력있는 성능을 보였다!






