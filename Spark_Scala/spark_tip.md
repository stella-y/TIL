## get max value from data frame
* Method 1: Use describe()
```scala
float(df.describe("A").filter("summary = 'max'").select("A").collect()[0].asDict()['A'])
```

* Method 2: Use SQL
```scala
df.registerTempTable("df_table")
spark.sql("SELECT MAX(A) as maxval FROM df_table").collect()[0].asDict()['maxval']
```

* Method 3: Use groupby()
```scala
df.groupby().max('A').collect()[0].asDict()['max(A)']
```
* Method 4: Convert to RDD
```scala
df.select("A").rdd.max()[0]
```

* spark context 에서 udf 만들기
```scala
sqlContext.udf.register("slice", (array : Seq[String], from : Int, to : Int) => array.slice(from,to))
```

* array concat
```scala
var df_news3=df_news2.withColumn("contents", concat_ws("\n", col("slice")))
```

* 각 row 를 다른 파일안에 저장하고 싶을 때
(rdd 에서 하는 법만 알아냄 / dataframe 에서 rdd 로 변환 후 사용)
```scala
rdd_df_news5.count()
sc.hadoopConfiguration.set("mapred.output.compress", "false")
rdd_df_news5.repartition(rows.toInt).saveAsTextFile("/user/stella/news_0701_10/")
```