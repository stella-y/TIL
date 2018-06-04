# DataFrame in spark

* 정형 구조의 dataset 의 rdd 를 다시 추상화
* python, panda 의 그것과 다름
    * 클러스터에 분산된 데이터셋 --> 데이터의 모든 행이 동일한 시스템에 저장되지 않음(로컬데이터가 아님)

```scala
spark.sparkContext
val prev=spark.read.csv("/user/stella/linkage")
prev.show()
prev.printSchema()

```

* 누락값 처리 등 간단한 가공 -> spark 의 csv reader 가 reader api 에서 설정할 수 있는 옵션을 통해 이 기능을 제공하고 있음
```scala
val parsed=spark.read
            .option("header", "true")
            .option("nullValue", "?")
            .option("inferSchema", "true")
            .csv("/user/stella/linkage")
parsed.printSchema()
```

* 데이터 프레임을 이미 존재하는 파일에 저장하려고 하면 오류가 발생함
    * Dataframewriter 의 savemode enum data 설정
    * overwrite, append, ignore(파일이 있으면 무시) 등


* dataframe 과 rdd 에 들어있는 데이터는 기본적으로 일시적
* 스파크에서는 이 데이터를 유지시키는 메커니즘을 제공
* cache method 호출 --> 데이터 프레임의 내용을 다음번 계산 때 메모리에 저장
 
* 데이터 유지 메커니즘 -> storagelevel 값으로 지정할 수 있음
    1.  persist(StorageLevel.MEMORY) (cache) : 직렬화하지 않은 자바 객체 형태로 저장
        * 파티션을 메모리에 올릴 수 없다고 판단하면 저장하지 않고 나중에 필요할 때 다시 계산할 것
        * 직렬화에 주는 부담을 피할 수 있어 --> 자주 호출되고, 빠른 응답이 필요할 때에 좋음
        * 단점
            * 다른 메커니즘보다 메모리를 많이 차지함
            * 작은 객체를 많이 유지하고 있어서 가비지 컬렉션에 부하를 줌
            * --> 일시적으로 시간을 벌 수 있어도 처리 속도는 느려짐
    2. MEMORY_SER 수준: 커다란 메모리 버퍼를 할당 / 레코드를 직렬화하여 저장
        * 적당한 포맷이 사용되면 직렬화 된 데이터는 그렇지 않은 데이터의 20%~50% 의 공간만 차지함
    3. cache on disk(MEMORY_AND_DISK / MEMORY_AND_DISK_SER) : 1,2와 달리 메모리에 올릴 수 없는 파티션을 디스크로 넘겨버림
        * DataFrame 과 RDD 모두 캐시 가능
            * dataframe 은 스키마 함께 사용하므로 rdd 보다 효율적으로 저장할 수 있음
            
*** 가비지 컬렉션 부하땜에 더 곤란해질 수 있으니 속도와 공간사이에서 절충 필요
여러 액션에서 데이터를 참조하고, 가용 메모리나 디스크의 크기가 상대적으로 작고, 다시 생성 비용이 큰 데이터를 캐싱하는게 좋음***
