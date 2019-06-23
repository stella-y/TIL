	• Spark : 통합 컴퓨팅 엔진과 클러스터환경에서 데이터를 병렬로 처리하는 라이브러리 집합
	• 통합 / 컴퓨팅 엔진 / 라이브러리
		○ 통합 - 데이터 분석 작업을 같은 연산엔진과 일관성 있는 api 로 수행할 수 있도록 설계
		○ 컴퓨팅 엔진 - 연산 역할만 수행할 뿐 영구 저장소의 역할은 수행하지 않음
			§ 애저 스토리지, 아마존 s3, 아파치 하둡, 아파치 카산드라, 아파치 카프카 등을 지원(데이터 저장위치 상관 없이 처리에만 집중)
		○ 라이브러리 - 궁극의 스파크 컴포넌트는 데이터 분석 작업에 필요한 통합 api 제공하는 통합엔진 기반의 자체 라이브러리
			§ Spark sql, mllib, graphx 등


	• 스파크 : 클러스터(여러 컴퓨터의 자원을 모아 하나의 컴퓨터처럼 사용)의 데이터 처리 작업을 관리하고 조율
	• 클러스터 구조 --> 클러스터 매니저가 관리
		○ 클러스터 매니저 - standalone, yarn, mesos 등
	• 클러스터 매니저
		○ 스파크 app 을 실행할 클러스터 머신 유지
		○ 사용자가 cluster manager 에 application 제출(submit)
		○ 클러스터 매니저는 이 application 실행에 필요한 자원 할당
		○ 드라이버 / 워커 실행시킴
	• Spark app
		○ Driver process / executor process 으로 구성된다아...
		○ Driver
			§ 클러스토 노드중 하나에서 실행됨 - main 함수 실행
			§ 스팍 앱 정보 유지 관리, 사용자 프로그램 입력에 대한 응답, 전반적인 executor 프로세스의 작업과 관련된 분석, 배포 & 스케쥴링 등등등…
			§ 물리적 머신의 프로세스 / 클러스터에서 실행중인 어플리케이션의 상태 유지
			§ (스파크 어플리케이션 실행 제어, 클러스터의 모든 상태정보 유지, 클러스터 매니저와 통신)
		○ Executor
			§ Driver 가 할당한 작업 수행
				□ 드라이버가 할당한 코드 실행 / 진행상황을 다시 드라이버에 보고
				□ 모든 스팍 app 은 개별 executor 프로세스 사용
	• Spark submit - application code 를 cluster 에 전송해 실행시킴
		○ Submit 명령 - class 지정 / cluster manager 형태 / 실행에 필요한 jar / 인수
	• Spark session instance
		○ 드라이버 프로세스
		○ 사용자가 정의한 처리 명령을 클러스터에 실행
	• Transformation / Action
	• Transformation
		○ 스파크의 핵심 데이터구조 - immutable --> 한번 생성하면 변경이 불가
			§ Ex - dataframe 을 한번 생성 --> immutable 한 것
		○ (action 하지않으면 실제 transformation 과정을 수행하지는 않지)
		○ 두가지 유형 - narrow dependency, wide dependency
			§ Narrow - 하나의 파티션이 하나의 출력파티션에만 영향을 줌
				□ 메모리에서만 작업
			§ Wide - shuffle(파티션 교환)이 일어나는 경우
				□ 셔플 결과를 디스크에 저장함
	• Spark - transformation 의 처리과정을 정의하는 분산 프로그래밍 모델
		○ 사용자 정의 transformation 은 DAG 로 표현
		○ Action - 하나의 job을 stage 와 task 로 나누고 dag 처리프로세스 실행
		○ Transformation 과 action 으로 다루는 논리적 구조가 dataset, dataframe 인 것
		○ Dataset, dataframe 을 새로 맨들려면 transformation 호출 / 연산을 시작하거나 사용한 언어에 맞는 데이터 타입으로 변환하려면 action 호출

	• Lazy evaluation - action 전까지 수행하진 않아 --> 실행될때에 전체 데이터 흐름을 최적화
	• 구조적 api(고수준) - dataframe, dataset, sql table, view
	• 저수준 api - rdd(분산 데이터 처리), 분산형 변수(브로드캐스트, 어큐뮬레이터처럼 분산형 공유 변수를 배포하고 다루기 위한 api)- 워커노드에 특정 변수를 공유시켜서 네트웍 없이 재사용하는 식인가봐
	• 
	• 

	• 구조적 api 실행과정
		1. Dataframe, dataset, sql 이용해 코드 작성
		2. 논리 실행계획으로 변환
			i. 추상적 transformation 만 표현
			ii. Driver, executor 정보를 고려하진 않는다
			iii. 카탈리스트 옵티마이저 (조건절, 선택절 부분에서 최적화)
		3. 물리 실행계획으로 변환
			i. 일련의 RDD와 transformation 으로 변환되는 것
		4. 물리실행계획 실행(RDD-저수준 프로그래밍 인터페이스)
			i. RDD를 대상으로 보든 코드를 실행(런타임에 전체 task, stage 를 제거할 수 있는 바이트코드 생성해 추가적 최적화 진행) 
	
	• 실행 모드
		○ 클러스터 모드
		○ 클라이언트 모드
			§ 클라이언트 머신에 스팍 드라이버가 위치함(스팍앱이 cluster 와 무관한 머신에서 동작함)
			§ --> gateway machine , edge node
				□ 클라 머신은 드라이버 프로세스 유지, 클러스터 매니저는 executor 프로세스 유지
		○ 로컬 모드
		

	• 스팍 생애주기(인프라 관점)
		○ Client 요청
			1. Spark application(컴파일된 jar,  lib 파일)제출
			2. 로컬 머신에서 코드가 실행
			3. 클러스터 드라이버에 요청(스팍 드라이버 프로세스 자원도 요청)
			4. 클러스터 노드 중 하나에 driver process 실행
			5. 잡을 제출한 client process 는 종료
			6. (driver process 가 cluster 에 배치됨)
		○ 시작
			1. 사용자 코드 실행(spark session 이 포함돼있을것)
			2. Spark session 은 spark cluster (driver & executor) 를 초기화
			3. 클러스터 매니저와 통신해서 스팍 executor process 실행 요청(submit 할 때 executor 수, 설정값 지정 가능)
			4. (스팍 클러스터(driver & executor) 생성된 것)
		○ 실행
			1. Driver 는 각 worker에 task 를 할당 / worker 는 성공, 실패 여부를 드라이버에 전송
		○ 완료
			

	• 스팍 생애주기(스팍 내부 관점)
		○ Spark session
			§ 모든 spark app 은 제일 먼저 spark session 을 생성함(대화형 모드에서는 자동생성)
				□  new SparkContext or SparkSession 의 builder method 를 사용해서 가능
				□ (builder method 를 쓰는걸 추천 - context 충돌 방지 등)
			§ 얘 생성하면 스팍 코드 실행이 가능해짐 - 이걸 이용해 모든 저수준 api, 기존 context, 관련 설정 정보에 접근 가능
		○ SparkContext
			§ 스팍 클러스터에 대한 연결을 나타냄
			§ RDD 같은 저수준 api 를 얘 통해 사용 가능하게 되는 것
			§ Spark session 으로 spark context 에 접근 가능해서 명시적 초기화는 필요 없으나 getOrCreate method 로 가능하긴 함
		○ 논리적 명령을 물리적 실행계획으로 변환
			§ 스팍코드 - transformation / action
			§ 파티션 재분배 / 값을 transformation / 집계, 최종결과
		○ 스팍 잡
			§ 보통 action 하나당 하나의 스팍잡 생성 (액션은 항상 결과를 반환함)
			§ 스팍잡은 일련의 스테이지로 나뉘고, 스테이지 수는 셔플 작업이 얼마나 많이 발생하는지에 따라 달라짐)
			§ Stage
				□ 다수의 머신에서 동일한 연산을 수행하는 태스크의 그룹
				□ 스팍은 가능한 많은 task 를 동일한 stage 에 묶으려 함
			§ Task
				□ 단일 executor 에서 실행할 데이터의 블록과, 다수의 트랜스포메이션 조합
				□ 데이터 단위(파티션)에 적용되는 연산단위
				□ --> 파티션 수를 늘리면 더 높은 병렬성을 얻을 수 있다!
		○ 세부 실행 과정
			§ 파이프라이닝
				□ 메모리나 디스크에 쓰기 전에 최대한 많은 단계를 수행하는 것
				□ Map 연산 후 다른 map 연산이 이어지면 함께 실행될 수 있게 stage 와 task 를 자동으로 연결
				□  e.g. map -> filter -> map 순의 연산이면 이 전 과정을 단일 stage 에 넣어버림
			§ 셔플 결과 저장(shuffle persistence)
				□ 스팍은 모든 셔플을 작업할 때에 데이터를 안정적인 저장소에 저장함 --> 여러잡에서 재사용할 수 있음
