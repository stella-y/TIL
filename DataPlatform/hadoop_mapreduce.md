## hadoop and mapreduce
* large scale computing 을 위해선, cluster architecture 가 필수적
* 이 때에 각 machine 에서의 fail 과 network 를 통한 copy 속도에 대한 영향을 최소화 하기 위해서 고안된 방법인 것
* storage infrastructure(file system) - hadoop system
* programming model - map-reduce

### hadoop
* **이용 가능한 데이터 형태**
	* 파일 사이즈가 큰 경우(gb\~tb)
	* rarely updated in place
	* reads and appends are common
* distributed file system
	* chunk server
		* file - contiguous chunck 로 나뉨
		* 각 chunk 는 16\~64mb
		* 각 chunk 는 replicated (2\~3개로)
		* 각 chunk 의 replica는 서로 다른 rack에 저장됨
	* master node
		* name node in HDFS
		* 파일이 어디에 저장돼있는지에 대한 meta data 를 저장
		* replicated 될 수 있음
	* client library for file access
		* chunk server 찾기 위해 master node 랑 통신
		* data 접근 위해서 chuck server 와 xhdtls

### map reduce
* map : sort and shuffle (extract something you care about)
* reduce : aggregate, summarize, filter or transform
* map-reduce 환경
	* **Partitioning** the input data
	* **Scheduling** the program's execution across a set of machines
	* Performing the **group by key** step
	* handling machine **failures**
	* managing required inter-machine **communication**
* dataflow
	* input and final output : stored on distributed file system
	* intermediate result : local file system of map reduce workds
* coordination
	* master node 가 control 함
	* task status : idle, in-progress, completed
	* master 가 worker 들에 주기적으로 ping 보내서 failure 여부 얻어냄
* dealing with failure
	* map work failure
		* completed 나 in-pregress 였던 worker 들의 map task 가 idle 로 reset 됨
		* reduce worker 들은 task 가 다른 worker 로 rescheduled 되면 notified 됨
	* reduce worker failure
		* inprogress 였던 것만 idle 로 reset
		* 다른 worker 에서 reduce task 재실행
	* master failure
		* map reduce task 자체가 abort 되고, client 에 notify 됨
* map reduce job 갯수
	* rule of thumbs
		* map 의 갯수를 cluster 의 node 보다 훨씬 크게 만든다.
		* map 하나에 dfs chunk 하나씩 대응시키는게 일반적임
		* 보통 reducer 수가 mapper 수보다 적다
* Refinements
	* slow worker 가 job completion time 을 엄청 늘어트리면(bad disk 등)
		* 단계가 거의 끝날때 작업의 백업 사본을 생성
	* map task 가 같은 key k 에 대해서 많은 값을 생성할 경우((k, v1), (k, v2), ...)
		* mapper 에서 미리 value 를 pre-aggregation 함 - combiner
			- combine(k, list(v1, ...)) --> (k, V)
		* combiner 는 reduce function 과 동일하게 작용
		* (단 이건 reduce function 이 commutative and associtive 할때만(통신을 야기하거나, 앞뒤로 연관성이 있거나))
		* 훨씬 적은 양의 데이터가 복사, shuffle 된다.


