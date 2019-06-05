## momgo to dataframe
1. dependency 에 mongo connector 추가
``` sbt
libraryDependencies += "org.mongodb.spark" %% "mongo-spark-connector" % "2.2.6"
```
2. sparksession builder 에서 mongodb 의 uri, db, collection 지정
```
mongodb.input.uri="mongodb://oscar-cruise.pg1.krane.9rum.cc/cruise.test"
```
```
import com.mongodb.spark.MongoSpark;
SparkSession spark=SparkSession.builder()
	.master("local")
	.appName("MongoSparkConnectorIntro")
	.config("spark.mongodb.input.uri", d)
```
2. 위의 2번 대신 read config 지정도 가능함
``` scala
val readConfig=ReadConfig(Map("uri" -> "mongodb://oscar-cruise.pg1.krane.9rum.cc", "database" -> "cruise",
                                "collection" -> "test"))
```
3. collection 전체 가져와서 잘 filter 해서 쓰자
``` scala
val cruise_all=spark.read.mongo(readConfig)
val filteredDF=cruise_all.filter(doc => doc.getAs[String]("type") == "movie")
```
