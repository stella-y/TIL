# Dataframe in spark
``` scala
parsed.count()
parsed.rdd.map(_.getAs[Boolean]("is_match")).countByValue()
parsed.groupBy("is_match").count().orderBy($"count".desc).show()
parsed.agg(avg($"cmp_sex"), stddev($"cmp_sex")).show()
```

생성한 모든 dataframe 을 db 테이블 처럼 다루면서 sql 로 질의할 수 있음
spark sql 실행엔진을 parsed data frame 과 연결하는 이름 지정
위에서 지정한 parsed 는 repl 세션 유지 동안만 사용할 수 있는 임시 테이블
구조화 된 데이터 셋의 스키마와 위치를 추적하는 하이브 메타스토어와 연결하도록 스파크 구성하면 spark sql 을 hdfs 에 저장된 테이블에 질의하는데 이용 가능
```scala
parsed.createOrReplaceTempView("linkage")
//임시 테이블을 spark sql 엔진에 등록
spark.sql("""
            SELECT is_match, COUNT(*) cnt 
            FROM linkage 
            GROUP BY is_match
            ORDER BY cnt DESC
          """).show()
```

hive-site.xml 파일 통해 하이브 메타스토어에 연결할 수 있으며 builder api sparksession 의 enable HiveSupport method 로 hiveql 을 사용할 수 있음
val sparkSession=SparkSession.builder.
master(“local[4]”).
enableHiveSupport().
getOrCreate()

```scala
val summary=parsed.describe()
summary.show()
summary.select("summary", "cmp_fname_c1", "cmp_fname_c2").show()

val matches=parsed.where("is_match=true")
val matchSummary=matches.describe()

val misses=parsed.filter($"is_match"===false)
val missSummary=misses.describe()
```

```scala
val schema=summary.schema
//쌓기 데이터 형태로
val longForm=summary.flatMap(row => {
    val metric=row.getString(0)
    (1 until row.size).map(i=> {
        (metric, schema(i).name, row.getString(i).toDouble)
    })
})
```
DataSet[T] / Dataframe 은 Dataset[Row]형의 별칭에 지나지 않는다!!!
암묵적 변환때문에 Dataset을 언제건 dataframe 으로 변환할 수 있다


```scala
val longDF=longForm.toDF("metric", "field", "value")
longDF.show()

val wideDF=longDF.
            groupBy("field").
            pivot("metric", Seq("count", "mean", "stddev", "min", "max")).
            agg(first("value"))
wideDF.select("field", "count", "mean").show()
```

```scala
//pivot.scala
//요약통계 데이터 프레임 재사용 위해
//쌓기 데이터로 변환 후 group by
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions.first

def pivotSummary(desc: DataFrame): DataFrame={
    val schema=desc.schema
    import desc.sparkSession.implicits._ //toDF 쓸라고(RDD to DataFrame conversion)
    val lf=desc.flatMap(row => {
        val metric=row.getString(0)
        (1 until row.size).map(i =>{
            (metric, schema(i).name, row.getString(i).toDouble)
        })
    }).toDF("metric", "field", "value")
    
    lf.groupBy("field").
        pivot("metric", Seq("count", "mean", "stddev", "min", "max")).
        agg(first("value"))
}
```