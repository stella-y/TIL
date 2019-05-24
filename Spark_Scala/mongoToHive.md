## mongodb to hive using spark
```scala
import com.mongodb.spark.MongoSpark;
SparkSession spark=SparkSession.builder()
	.master("local")
	.appName("MongoSparkConnectorIntro")
	.config("spark.mongodb.input.uri", d)
```
참고 : https://docs.mongodb.com/spark-connector/current/java/datasets-and-sql/