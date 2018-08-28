## one hot encoding
```scala
import org.apache.spark.ml.feature.{OneHotEncoder, StringIndexer}

val df = spark.sql("select buy_lev3 from user_stella.cross_domain_gift_more3_train_item_attr")

val indexer=new StringIndexer()
    .setInputCol("buy_lev3")
    .setOutputCol("buy_lev3_index")

val indexed=indexer.transform(df)

val encoder=new OneHotEncoder()
    .setInputCol("buy_lev3_index")
    .setOutputCol("buy_lev3_vec")
val encoded=encoder.transform(indexed)
encoded.show()
```

## vector 합치기
```scala
import org.apache.spark.ml.feature.VectorAssembler

var assembler=new VectorAssembler().
        setInputCols(Array("amt", "item_type_index", "buy_lev3_vec", "brand_lev2_vec")).
        setOutputCol("agg_item_vec")
```