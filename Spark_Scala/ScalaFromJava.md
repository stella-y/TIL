#자바 --> 스칼라

``` scala
object HelloWorld {
  def main(args: Array[String]) {
    println("Hello, world!")
  }
}
```
* main 함수부터
	* main 함수를 클래스 대신 싱글턴 객체 안에 생성
	*  **스칼라에는 static 개념이 없음!(함수든 필드든)**
		* 이게 필요해지면 싱글턴 객체 안에 선언함
* 스칼라 컴파일 & 실행하기
	1. scalac 컴파일
		``` shell
		scalac HelloWorld.scala```
		클래스 파일 몇개 생성 --> 스칼라 명령으로 바로 실행 가능한 클래스
	2.  실행
		``` shell
			scala -classpath . HelloWorld
		```
		일단 컴파일 되면 Scala 프로그램은 scala 명령을 통해 실행
		자바와 매우 유사함
* 자바와 함께 사용(java class import)
	* 사용하고 싶은 Java 클래스는 임포트 하면 됨
	* java.lang 패키지의 모든 클래스는 임포트 하지 않아도 기본적으로 사용 할 수 있음
	``` scala
	import java.util.{Date, Locale}
	import java.text.DateFormat
	import java.text.DateFormat._
	object FrenchDate {
  		def main(args: Array[String]) {
	    val now = new Date
	    val df = getDateInstance(LONG, Locale.FRANCE)
	    println(df format now)//요기요기요기!
	  }
	}```
	* \* 대신 _ 씀
	* df format now == df.format(now)
* 다 객체다
	* 숫자, 함수 뭐 전부 다
	1. 숫자
		*  1 + 2 * 3 / x --> (1).+(((2).\*(3))./(x)) 이렇게 써야함
			* 렉서가 토큰들 중에 가장 긴 부분을 찾아버려서 1. 이렇게 쓰면 double 로 바꿔버려
	2. 함수
				* 함수에 함수를 인자로 넘기기
				* 함수를 변수에 저장하기
				* 함수가 함수 리턴하기
		* 위에꺼 다 가능
		``` scala
			object Timer {
			  def oncePerSecond(callback: () => Unit) {
			    while (true) { callback(); Thread sleep 1000 }
			  }
			  def timeFlies() {
			    println("time flies like an arrow...")
			  }
			  def main(args: Array[String]) {
			    oncePerSecond(timeFlies)
			  }
			}```
		* 행동을 매초 수행해야할 때에 --> 타이머 함수가 목적함수 실행하게 --> (UI 코드에서 이벤트 발생시의 콜백 함수 등록...)
			* 콜백함수를 인자로 받는 타이머 함수 구현
			* 이때에 함수의 type 이 **()=> Unit**
				* 인자 안받고 암것도 안돌려주는 함수
				* unit --> void 와 유사





https://docs.scala-lang.org/ko/tutorials/scala-for-java-programmers.html 참고후 정리