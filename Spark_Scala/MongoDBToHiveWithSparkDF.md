# 대용량 mongodb 데이터를 hive 테이블로 소싱하는 방법
* 몽고 디비에 적재된 데이터를 spark dataframe 을 이용하여 hive 테이블로 소싱하는 방법
* 크루즈 데이터와 같이 document 간 schema 변형이 심하고, 사이즈가 매우 큰 데이터의 경우에 필요해지는 내용들을 정리해봤다.

## mongo connector
* mongo db 와 spark 를 연결할 커넥터 필요
* https://docs.mongodb.com/spark-connector/master/scala/read-from-mongodb/
* Trouble shooting
	* 큐싯에서 받고 있는 lz4 라이브러리와 충돌하여 에러가 생기므로 아래와 같이 설정하여 이를 방지한다.
	```
	//build.sbt
	libraryDependencies += ("com.kakao.cuesheet" %% "cuesheet" % "0.10.1.10-spark2.4.0-hadoop2.6.5")
	  .excludeAll( ExclusionRule("net.jpountz.lz4", "lz4"),
	    ExclusionRule("org.lz4", "lz4-java"))
	libraryDependencies += "org.mongodb.spark" %% "mongo-spark-connector" % "2.2.6"
	```
	* 큐싯을 사용할 경우 spark session 설정 관련해서는 application.conf 를 이용하면 되지만, 이보다 아래에서처럼 설정하는게, 코드 수정에 용이하다.
```scala
import spark.implicits._
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise",
  "collection" ->"2019-04-25"))
val cruise_all=spark.read.mongo(readConfig)
val filteredDF=cruise_all.filter(doc => doc.getAs[String]("type") == "movie")
```

## spark 의 type과 schema
### Type and schema inferencing
* spark 는 전체 데이터의 일부를 샘플링하여, collection 의 schema 와 column 의 type을 inferencing 을 한다.
* 그렇기때문에 사전에 스키마나 type 설정을 확실하게 하지 않는 nosql db 를 읽어올떄에는 이 sampling size 가 부족할 수 있다.
* (csv 파일이건, db 에서부터 데이터를 읽어오건 마찬가지)
* 아래와 같이 schema inferencing 을 위한 sampling size 를 늘릴 수도 있다. (default =1000)
```scala
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise",
  "collection" ->"2019-04-25", "sampleSize" -> "100000"))
val cruise_all=spark.read.mongo(readConfig)
```

### Schema 설정
#### schema infering 해제 후, struct 로 schema 설정
* read config 에서 'inferSchema' 옵션을 'false'로 바꿔두면, spark 에서 schema infering 을 하지 않게 된다.
* 예시가 될 수 있는 json type data 를 먼저 넣어두고, 이의 schema를 struct 형태로 가져와서 이를 mongodb config 에 세팅하여 이를 기준으로 schema 를 읽어올 수 있게 한다.
* 여기서 json type data 에서 읽고 싶은 struct 가 어디까지인지 미리 세팅해두면, mongodb 에서도 그 schema 그대로 데이터를 그대로 읽어오므로, column customizing 또한 쉬워진다
```scala
val json_cols=movie_sample_df.columns.toSeq
movie_sample_df.select(json_cols.map(col): _*)
 
val df_outer=movie_sample_df.select(json_cols.map(c =>
  movie_sample_df.schema(c).dataType match {
    case struct: StructType => to_json(col(c)).as(c)
    case _ => col(c).cast("string")
  }): _*)
df_outer.printSchema()
df_outer.show()
 
val json_outer_schema=df_outer.schema
println(json_outer_schema)
 
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise"
  , "collection" ->"2019-04-25", "inferSchema"-> "false"
))
val cruise_all=spark.read.schema(json_outer_schema).mongo(readConfig)
```

## Partitioning
### partitioner and partition key setting
#### partitioner 설정
* 읽어오려는 대상 데이터가 매우 클 경우 아래와 같이 default partitioner 가 실패했다는 에러 메시지가 나온다.
* 몽고디비에는 아래와 같은 parititioner 가 있으니, 데이터에 맞는 partitioner 를 선정해준다.
	* https://docs.mongodb.com/spark-connector/master/configuration/#partitioner-conf
		1. MongoDefaultPartitioner
		2. MongoSamplePartitioner
		3. MongoShardedPartitioner
		4. MongoSplitVectorPartitioner
		5. MongoPaginateByCountPartitioner
		6. MongoPaginateBySizePartitioner
* partitioner 설정 코드는 아래와 같다.
```scala
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise"
    , "collection" ->"2019-04-25", "inferSchema"-> "false", "partitioner" -> "MongoPaginateByCountPartitioner"
    , "partitionerOptions.numberOfPartitions" -> "64"
  ))
val cruise_all=spark.read.schema(json_outer_schema).mongo(readConfig)
```

#### partition key 설정
* partitioner 를 변경하더라도 partition key 설정이 잘못됐을 경우 아래와 같은 에러메시지를 볼 수 있다.
```
[ERROR] 2019-06-20 16:15:06,996 com.mongodb.spark.rdd.MongoRDD -
——————————————
WARNING: Partitioning failed.
——————————————
 
Partitioning using the 'MongoPaginateByCountPartitioner' failed.
 
Please check the stacktrace to determine the cause of the failure or check the Partitioner API documentation.
Note: Not all partitioners are suitable for all toplogies and not all partitioners support views.%n
 
——————————————
 
[ERROR] 2019-06-20 16:15:07,034 org.apache.spark.deploy.yarn.ApplicationMaster - User class threw exception: com.mongodb.MongoQueryException: Query failed with error code 96 and error message 'Executor error during find command :: caused by :: Sort operation used more than the maximum 33554432 bytes of RAM. Add an index, or specify a smaller limit.' on server oscar-cruise.pg1.krane.9rum.cc:27017
com.mongodb.MongoQueryException: Query failed with error code 96 and error message 'Executor error during find command :: caused by :: Sort operation used more than the maximum 33554432 bytes of RAM. Add an index, or specify a smaller limit.' on server oscar-cruise.pg1.krane.9rum.cc:27017
```
* partition key 로는 되도록 mongo db 에서 이미 indexing 되어있는 key 를 가져 오는 것이 좋다.
```scala
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise"
    , "collection" ->"2019-04-25", "inferSchema"-> "false", "partitioner" -> "MongoPaginateByCountPartitioner"
    , "partitionerOptions.partitionKey" -> "_id", "partitionerOptions.numberOfPartitions" -> "64"
  ))
val cruise_all=spark.read.schema(json_outer_schema).mongo(readConfig)
```

### 기타
#### schema 와 맞지 않는 데이터 처리 옵션
* Set mode to DROPMALFORMED --> this will drop the lines that don't match the schema
* Set mode to PERMISSIVE --> this will set the whole line to null values
* Set mode to FAILFAST --> this will throw an exception when a mismatch is discovered
```scala
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise",
  "collection" ->"2019-04-25", "sampleSize" -> "10000", "mode" -> "DROPMALFORMED"), "maxMalformedLogPerPartition", 10000)
```

#### case class 로 explicit schema 설정
* schema 가 확실한 경우에는 아래와같이 미리 case class 를 이용해 미리 dataframe 의 schema 를 구성해둘 수 있다
	* 크루즈데이터와같이 크고 복잡한 형태의 스키마가 필요한 경우엔 물론 이런식의 수동 설정이 쉽지 않다.
```scala
case class Character(name: String, age: Int)
val explicitDF = MongoSpark.load[Character](sparkSession)
 
explicitDF.printSchema()
 
/*
root
 |-- name: string (nullable = true)
 |-- age: integer (nullable = false)
*/
```
* 예시가 될만한 json file 을 미리 넣어둔 후, 이의 schema를 schema inferencing 으로 얻어온 후 그 schema 에 맞게 만들 수도 있다.
	* 하지만 이경우 대상 json element 중 하나라도 type 이 다른 경우(struct type → string type 등) 문제가 생긴다
```scala
val path="./movie_sample2.json"
val movie_sample_df=spark.read.json(spark.sparkContext.wholeTextFiles(path).values)
 
val df=filteredDF.select($"data.*")
val json_df=movie_sample_df.select($"data.*")
 
 
val df_cols=df.columns.toSet
val json_cols=json_df.columns.toSet
val total=df_cols++json_cols
 
 
val json_df_1=json_df.select(expr(json_cols, total): _*)
json_df_1.printSchema()
 
val json_df_2=structToString(json_df_1)
json_df_2.printSchema()
val new_json_cols=column_endswith(json_df_2)
println(new_json_cols)
 
val json_toUnion=json_df_2.select(new_json_cols.map(col): _*)
 
val df_1=df.select(expr(df_cols, total): _*)
df_1.printSchema()
 
val df_2=structToString(df_1)
df_2.printSchema()
 
val new_df_cols=column_endswith(df_2)
println(new_df_cols)
 
val df_toUnion=df_2.select(new_df_cols.map(col): _*)
 
 
json_toUnion.show(20, false)
df_toUnion.show(20, false)
json_toUnion.printSchema()
df_toUnion.printSchema()
 
val unionDF=json_toUnion.union(df_toUnion)
unionDF.show(20, false)
```

#### column 임의 설정
* schema 에 있어야 할 column 이 없는 경우에도 에러가 발생한다. 이 경우 아래와 같이 임의로 컬럼을 만들어준 후 의미없는 값을 넣어 에러를 방지할 수 있다
```scala
def expr(myCols: Set[String], allCols: Set[String]) = {
  allCols.toList.map(x => x match {
    case x if myCols.contains(x) => col(x)
    case _ => lit("").as(x)
  })
}
```

#### 임의로 type 변경
* 기본적으로 json type 의 element 는 spark 에서는 structure type 으로 인식한다. 그렇기때문에, json 내부의 구조또한 맞지 않을경우 에러를 발생 시킨다. 이런 경우 아래와 같이 json type 자체를 string 으로 변환하여 이용할 수 있다
```scala
val df_outer=movie_sample_df.select(json_cols.map(c =>
  movie_sample_df.schema(c).dataType match {
    case struct: StructType => to_json(col(c)).as(c)
    case _ => col(c).cast("string")
  }): _*)
 
 
/*******************또는*******************/
def structToString(df : DataFrame): DataFrame={
  val cols=df.columns.toSeq
 
  var new_df=df
  for (c <- cols){
    //println(c)
    df.schema(c).dataType match {
      case struct: StructType => new_df=new_df.withColumn(c.toString+"2", to_json(col(c)))
      case struct: ArrayType => new_df=new_df.withColumn(c.toString+"2", to_json(col(c)))
      case _ => new_df=new_df.withColumn((c.toString+"2"), col(c))
    }
  }
  new_df
}
```

* 위와 같은 방법으로 해결이 되는 경우도 있으나 이미 json 대신 string value 만 들어가 있는 경우에는 casting error 가 발생된다.
```
Caused by: org.apache.spark.SparkException: Job aborted due to stage failure: Task 101 in stage 1.0 failed 4 times, most
```