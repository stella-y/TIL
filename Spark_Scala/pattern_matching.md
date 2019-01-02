## 패턴 매칭
* e.g.
```scala
object MatchTest1 extends App {
  def matchTest(x: Int): String = x match {
    case 1 => "one"
    case 2 => "two"
    case _ => "many"
  }
  println(matchTest(3))
}
```
* e.g.
```scala
source=pf
val outputTbName = source match {
      case "talk" => s"db_name.tb_talk_${idType}"
      case "pf" =>s"db_name.tb_${idType}_${source}"
    }
```

https://docs.scala-lang.org/ko/tutorials/tour/pattern-matching.html.html