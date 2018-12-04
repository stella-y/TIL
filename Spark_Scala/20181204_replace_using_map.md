## Replace using map and regular expression
* replace using regular expression
	* regular expression 은 string 에 .r 로 표기해주면 됨
	* regular_expression.replaceAllIn(string, "x")로 expression 등장시 어떻게 변환할지를 지정해주면 된다
```scala
var reg_list=List("[/.]+".r, "[/!]+".r)
reg_list(0).replaceAllIn(test_string, "x")
```
* map 은 python 에서의 dictionary 쯤으로 생각하면 될 듯
```scala
var reg_map=Map("[/.]+".r -> "_._", "[/!]+".r -> "_!_")
var test_string="[서소문사진관]휴일 돌풍·벼락·폭우.. 비 피해도 잇따라!! asdf"
for ((k, v) <- reg_map) test_string=k.replaceAllIn(test_string, v)
```
* 함수로 정의
```scala
reg_map=Map("[/.]+".r -> " _._ ",
            "[/,]+".r -> " _,_ ",
            "[/!]+".r -> " _!_ ",
            "[/?]+".r -> " _?_ ",
            "[/!?]+".r -> " _!?_ ",
            "[/;]+".r -> " _;_ ",
            "[/~]+".r -> " _~_ ",
            "[/-]+".r -> " _-_ ",
            "[/♪♬]+".r -> " _♪♬_ ",
            "[/ㅋ]+".r -> " _ㅋ_ ",
            "[/ㅎ]+".r -> " _ㅎ_ ",
            "[/ㅉ]+".r -> " _ㅉ_ ",
            "[/ㄴ]+".r -> " _ㄴ_ ",
            "[/ㅌ]+".r -> " _ㅌ_ ",
            "[/ㅊ]+".r -> " _ㅊ_ ",
            "[/ㅜ]+".r -> " _ㅜ_ ",
            "[/ㅠ]+".r -> " _ㅠ_ ",
            "[/ㅜㅠ]+".r -> " _ㅜㅠ_",
            "\\[".r -> " _[_ ",
            "\\]".r -> " _]_ ",
            "\"".r -> " _\"_ ",
            "\\'".r -> " _'_ ")
def term_replace(s: String)={
    var test_string=s
    for ((k, v) <- reg_map) test_string=k.replaceAllIn(test_string, v)
    test_string
}
```
* 이걸 다시 udf 로 변환하여 dataframe 에 적용
```scala
import org.apache.spark.sql.functions.udf 
val term_replaceUDF=udf[String, String](term_replace)
df_test.select(term_replaceUDF(col("title")).as("cleaned_title")).show(10, false)
'''
+----------------------------------------------+
|cleaned_title                                 |
+----------------------------------------------+
|[서소문사진관]휴일 돌풍·벼락·폭우 _._  비 피해도 잇따라            |
|허익범 특검 _,_  댓글조작 공범 '서유기' 불러 6시간 조사           |
|[미디어 세상]이방인을 '혐오'하는 언론들                       |
|전남 해안 호우경보 확대 _._ 전국에 강한 비 '태풍 주의'            |
|[날씨] 월요일 _,_  전국 장맛비 _._ 태풍 '쁘라삐룬' 북상         |
|금융그룹 통합감독 개시 _._  발등에 불 떨어진 삼성                |
|위안부 피해자 김복득 할머니 별세 _._ 남은 생존자 27명             |
|임주희 _,_  아티스트로 자라난 피아노 신동 _._ 국내 첫 리사이틀       |
|내일도 많은 비 _._ "중부지방 시간당 30mm"                  |
|[날씨] 전국 모레까지 최고 300mm 큰비 _._ 태풍 내일 저녁 제주 해상 접근|
+----------------------------------------------+
only showing top 10 rows
'''
```