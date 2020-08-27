# Chapter2. 스파크는 어떻게 동작하는가
- 스파크 
	- 분산 데이터 처리에 사용(맵리듀스에 대한 대안으로 언급됨)
	- 메모리 기반 처리, 지연 평가방식으로 효율을 극대화

### 스파크 컴포넌트
- 스파크 생태계
	- Spark Core
	- Spark SQL
	- Spark MLlib
	- Spark Streaming
	- Spark GraphX
- Spark core
	- 가장 핵심적인 데이터 처리 framework
	- RDD 기반
		- RDD : 지연평가를 수행하면서 정적인 데이터 타입을 가지는 분산 데이터 모음
- Spark SQL
	- spark core 와는 다른 질의 최적화 엔진을 갖고 있어서 성능에 대해 전혀 다른 고려사항을 검토해야함
	- DataFrame, Dataset 데이터 타입 interface 정의
		- 2.0 부터 dataset, dataframe 이 통합됐고, dataset은 row객체를 가진 dataframe 이며 필드 번호로 접근함
	- spark core만으로 할 수 있는 일도 spark sql과 함께 적용해서 성능을 극대화시킬 수 있음
- SparkMLlib, SparkML
	- MLlib
		- 거의 spark api 기반으로만 작성되어 spark core와 동일한 원리 기반으로 성능 결정
		- RDD 기반
	- ML
		- Dataframe 기반

### 스파크의 병렬 연산모델 : RDD
- 변경할 수 없는 형태의 분산된 객체들의 모음 Resilient Distributed Dataset
- executor or slave node 에 저장됨
- partition 객체로 구성됨
- **클러스터 매니저**가 executor 들을 실행해주고 분산해주는 역할을 하고, **스파크 실행엔진**이 executor 들에게 데이터를 분산해주고 실행을 요청함
- **지연평가**, **인메모리 저장소**, **불변성의 패러다임**

#### 지연 평가
- 파티션은 액션이 호출되기 전까지는 계산되지 않는다.
	- 액션
		- RDD 가 아닌 다른 type 의 결과를 리턴하는 스파크 연산의 한 종류
			- 데이터를 드라이버로 돌려주거나(count, collect 등)
			- 데이터를 외부 저장소에 저장하는 등
		- execution plan
			- 액션 스케쥴러 시작되면 RDD transformation 간의 dependancy 를 바탕으로 DAG 생성
			- 최종 partition 생성을 위해 필요한 각 단계를 정의하기 위해 역으로 거슬러 올라가는 방식으로 action 평가
- 장점
	- 드라이버와 통신할 필요가 없는 연산들을 통합하여 데이터가 여러 단계를 거치지 않도록 한다.
		- e.g. map, filter 함수 호출시 이 수행 명령을 합쳐서 executor 에 보냄 --> 레코드에 한번만 접근하고도 연산이 가능해짐 (연산 복잡성이 절반이 됨)
	- 개발이 쉬워진다
		- 직접 연관성이 있는 연산들을 엮어놓기만 하면 이들을 합쳐주는 작업은 스파크의 평가 엔진이 처리해준다
		- e.g. 단어세기 문제 만들때 def 안에 필요한 각 과정 풀어놓는 것
- 장애 내구성
	- 각 파티션이 자신을 재계산하는데 필요한 종속성 등의 데이터를 갖고 있음
		- 데이터 변경내역 등이 로그로 유지될 필요가 없음
		- 이미 데이터가 다 있으미 빠른 복구를 위해 병렬 연산을 수행할 수도 있음]

#### 메모리 영속화(in-memory persistence)와 메모리 관리
- in-memory 방식으로 반복 연산이 들어있는 경우 성능상 우위를 갖게 됨
- 데이터가 거치는 단계마다 디스크에 기록하는 대신 executor memory 에 데이터를 로드해놓을 수도 있음
- 메모리 관리옵션 세 가지
	1. 메모리에 직렬화되지 않은 자바 객체
		- 원본의 자바객체
		- 직렬화 연산 안하니깐 가장 빠르지만 메모리 공간 사용은 비효율적임
	2. 메모리에 직렬화된 데이터
		- network로 전송 가능한 byte stream으로 변환
		- 직렬화된 데이터를 읽을때 cpu 가 많이 사용돼서 느려짐
		- 메모리 사용 측면에서는 뛰어남 (kryo 직렬화 쓰면 더더욱)
	3. 디스크
		- 램에 담기에 파티션이 너무 큰 RDD 의 경우
		- 반복 연산에는 속도면에서 불리함
- persist() 함수
	- 사용자가 RDD 를 어떻게 저장할지 결정할 수 있게 해준다
	- 기본적으로 RDD 를 메모리에 직렬화되지 않은 상태로 저장하지만 인자 수정해서 저장방식 제어 가능함

#### 불변성과 RDD 인터페이스
- RDD의 각 타입이 구현해야만 하는 속성을 RDD 인터페이스에 정의해놓음
	- 실행 엔진이 RDD 를 계산하는데 필요한 데이터 위치 정보 혹은 RDD 의 종속성 등
- transformation 을 통해 새 속성을 가진 RDD 를 생성(immutable 하므로)
- RDD 생성방법
	1. 기존 RDD 에 transformation
	2. SparkContext 객체로부터 생성
	3. DataSet이나 DataFrame을 변형한 것 (SparkSession(SQLContext)로부터 만들어짐)

#### 넓은 종속성 vs 좁은 종속성
- transformation의 두 가지 종류
- 좁은 종속성
	- 자식 RDD 의 각 파티션이 부모 RDD 의 파티션들에 대해 단순하고 한정적인 종속성을 가지는 것
	- 1. 디자인 시점에 종속성을 결정할 수 있고 / 2. 부모 파티션의 값과 상관 없고 / 최대 하나의 자식파티션을 가질 때
	- 즉, 다른 파티션의 정보를 필요로 하지 않고 데이터의 임의의 부분에 대해 실행이 가능
	- e.g. map or coalesce 등
- 넓은 종속성
	- 임의의 데이터만으로 실행이 불가능함(키값에 따라 파티셔닝 된 데이터를 요구하는 등)
	- e.g. sort, reduceByKey, groupByKey, join, rePartition 등

### 스파크 잡 스케쥴링
- 하나의 spark cluster 는 여러개 spark application 을 동시에 실행할 수 있다.
- spark application
	- application 들은 cluster manager 에 의해 스케쥴링 되고, 각 하나의 SparkContext를 가짐
	- driver process, executor process 로 구성
- job들은 application 의 한 RDD 가 호출하는 각 action 에 대응

### 스파크 잡 해부
- job
	- 액션 하나에 대응됨
	- 각 액션은 spark application 의 driver의 프로그램에서 호출됨
	- DAG의 edge 는 RDD transformation 에서 파티션들간의 종속성을 기반으로 그려짐 --> DAG leaf node 가 action
	- application 은 action 을 호출한 최종 RDD 를 평가하기 위해 필요한 transformation 들을 포함한 잡을 바로 실행함
- stage
	- action 은 하나 이상의 transformation 을 가지고, 넓은 transformation 은 잡의 부분들을 stage 로 정의함
	- 즉, 각 stage는 넓은 transformation 에서 생성되는 셔플 의존성에 대응한다.
	- 하나의 stage 는 다른 executor 나 driver 와의 통신 없이 하나의 executor 에서 계산 가능한 태스크들의 집합
	- 새로운 stage 는 언제든지 노드들 사이에서 네트워크 통신이 요구될 때마다 시작된다.(셔플 등)
	- 통신이 요구되기때문에 순차적으로 실행되어야함
	- 프로그램이 최소한의 셔플로 수행될 수 있게 설계하는게 바람직할 것
- task
	- 실행 계층에서 가장 작은 단위
	- 한 stage 의 모든 task 들은 서로 다른 데이터를 대상으로 동일한 코드를 실행한다.
	- 한 task 는 둘 이상의 executor 에서 실행될 수 없다.
	- stage 당 task 갯수는 해당 스테이지 결과의 RDD 파티션 갯수에 대응된다.
	- cluster는 각 stage마다 필요한 모든 task 를 동시에 실행시킬 수는 없다.
		- 각 executor 는 사용하는 core수가 정해져있는데 대개는 cluster 의 물리적 	core 갯수와 대응된다.
		- spark application 에 할당된 executor core 갯수의 총합보다 더 많은 태스크를 동시에 실행할 수는 없다.
		- 동시에 실행되는 task 의 수 =(executor core 총 합=executor 당 core 갯수 \* executor 갯수)
		- 태스크 실행을 위한 슬롯보다 더 많은 파티션(태스크)가 있다면 처음 실행된 task 가 끝난 다음에 할당 되어 실행될 것
- 정리
	- job : 하나의 최종 결과를 연산해 내는 데 필요한 RDD transformation 들의 집합
	- stage : 작업의 한 부분 / 드라이버의 도움 없이 완료 가능 (파티션끼리 데이터 전송 없이 연산 가능한 단위)
	- task : 각 파티션에 대한 작업을 수행하는 단위



