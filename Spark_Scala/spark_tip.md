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

* concate two or more columns
```scala
import org.apache.spark.sql.functions.{concat, lit}

df.select(concat($"k", lit(" "), $"v"))
```
```scala
df = df.withColumn('joined_column', 
                    sf.concat(sf.col('colname1'),sf.lit('_'), sf.col('colname2')))
df.show()
```