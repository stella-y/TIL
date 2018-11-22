# DataFrame in spark

* 정형 구조의 dataset 의 rdd 를 다시 추상화
* python, panda 의 그것과 다름
    * 클러스터에 분산된 데이터셋 --> 데이터의 모든 행이 동일한 시스템에 저장되지 않음(로컬데이터가 아님)

```scala
spark.sparkContext
val prev=spark.read.csv("/user/stella/linkage")
prev.show()
>>+-----+-----+-----------------+------------+------------+------------+-------+------+------+------+-------+--------+
|  _c0|  _c1|              _c2|         _c3|         _c4|         _c5|    _c6|   _c7|   _c8|   _c9|   _c10|    _c11|
+-----+-----+-----------------+------------+------------+------------+-------+------+------+------+-------+--------+
| id_1| id_2|     cmp_fname_c1|cmp_fname_c2|cmp_lname_c1|cmp_lname_c2|cmp_sex|cmp_bd|cmp_bm|cmp_by|cmp_plz|is_match|
|37291|53113|0.833333333333333|           ?|           1|           ?|      1|     1|     1|     1|      0|    TRUE|
|39086|47614|                1|           ?|           1|           ?|      1|     1|     1|     1|      1|    TRUE|
|70031|70237|                1|           ?|           1|           ?|      1|     1|     1|     1|      1|    TRUE|
|84795|97439|                1|           ?|           1|           ?|      1|     1|     1|     1|      1|    TRUE|
|36950|42116|                1|           ?|           1|           1|      1|     1|     1|     1|      1|    TRUE|
|42413|48491|                1|           ?|           1|           ?|      1|     1|     1|     1|      1|    TRUE|

prev.printSchema()
>>root
 |-- _c0: string (nullable = true)
 |-- _c1: string (nullable = true)
 |-- _c2: string (nullable = true)
 |-- _c3: string (nullable = true)
 |-- _c4: string (nullable = true)
 |-- _c5: string (nullable = true)
 |-- _c6: string (nullable = true)
 |-- _c7: string (nullable = true)
 |-- _c8: string (nullable = true)
 |-- _c9: string (nullable = true)
 |-- _c10: string (nullable = true)
 |-- _c11: string (nullable = true)
```

* 누락값 처리 등 간단한 가공 -> spark 의 csv reader 가 reader api 에서 설정할 수 있는 옵션을 통해 이 기능을 제공하고 있음
```scala
val parsed=spark.read
            .option("header", "true")
            .option("nullValue", "?")
            .option("inferSchema", "true")
            .csv("/user/stella/linkage")
parsed.printSchema()
>>root
 |-- id_1: integer (nullable = true)
 |-- id_2: integer (nullable = true)
 |-- cmp_fname_c1: double (nullable = true)
 |-- cmp_fname_c2: double (nullable = true)
 |-- cmp_lname_c1: double (nullable = true)
 |-- cmp_lname_c2: double (nullable = true)
 |-- cmp_sex: integer (nullable = true)
 |-- cmp_bd: integer (nullable = true)
 |-- cmp_bm: integer (nullable = true)
 |-- cmp_by: integer (nullable = true)
 |-- cmp_plz: integer (nullable = true)
 |-- is_match: boolean (nullable = true)
```

## type지정 통한 성능향상
* spark 은 스키마 유추 위해서 데이터셋을 두번 읽게 됨
    1. 읽으면서 각열의 데이터 타입 파악
    2. 다시 읽으면서 실제 파싱 수행
* 그렇기때문에 스키마 미리 알고있다면 org.apache.spark.sql.types.StructType의 인스턴스 생성해서 schema 함수 통해서 reader api 에 미리 넘겨주는게 성능 향상에 좋다!

## 읽기 가능 형식
* json, parquet, orc, odbc, libsvm, text. 등
``` scala
val d1=spark.read.format("json").load("file.json")
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
