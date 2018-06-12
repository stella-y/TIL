%md
# 자바 --> 스칼라

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
		scalac HelloWorld.scala
		```
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
	}
	```
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
			}
		```
		* 행동을 매초 수행해야할 때에 --> 타이머 함수가 목적함수 실행하게 --> (UI 코드에서 이벤트 발생시의 콜백 함수 등록...)
			* 콜백함수를 인자로 받는 타이머 함수 구현
			* 이때에 함수의 type 이 **()=> Unit**
				* 인자 안받고 암것도 안돌려주는 함수
				* unit --> void 와 유사
* 케이스 클래스 & 패턴매칭
	* 상속 트리구조
		* 자바라면 추상 상위클래스 / 노드, 리프 각각에 대한 실제 하위 클래스 정의했을 것
		* 스칼라에서는 이때에 케이스 클래스 이용!
	* **케이스 클래스**
	``` scala
		abstract class Tree
		case class Sum(l: Tree, r: Tree) extends Tree
		case class Var(n: String) extends Tree
		case class Const(v: Int) extends Tree
	```
		* instance 생성시 new 생략 가능
		* getter 함수 자동 정의됨 / i.v 로 접근 가능(i : instance / v : parameter)
		* equals / hashCode도!! --> 구조적 동일함 확인(생성된 곳이 달라도 각각의 생성자 파라미터 값이 같으면 같은걸로 여김)
		* **패턴 매칭** 통해서 따로 사용될 수 있다
			* (환경 - 변수마다 주어진 값들을 저장해 두는 곳)
			* 환경 대신 데이터 저장용으로 함수 직접 쓰기 (환경이 변수 명에서 값으로 가는 함수에 지나지 않는다고 생각할수도 있는 것)
				``` scala
				{ case "x" => 5 }
				```
				x가 인자로 들어올 때 5 리턴
			* 환경 타입에 이름 붙여주기
				``` scala
				type Environment = String => Int
				```
				String 에서 int 로 가는 함수타입의 다른 이름
			``` scala
			def eval(t: Tree, env: Environment): Int = t match {
			  case Sum(l, r) => eval(l, env) + eval(r, env)
			  case Var(n)    => env(n)
			  case Const(v)  => v
			}
			```
			* 패턴 매칭의 기본 아이디어!
				**대상이 되는 값을 여러가지 관심있는 패턴에 순서대로 맞춰본 후, 맞는 것이 있으면 맞는 값 중 관심있는 부분에 대해 새로 이름 붙이고, 그 이름 붙인 부분을 사용하는 어떤 작업을 진행!**
			* 멤버함수 사용과 비교
				* 멤버함수 쓰는 경우 : 
					새 노드 추가하려면 하위 클래스 그냥 정의하면 됨
					근데 트리에 새로운 연산 추가하는 작업이 어려움(tree 의 모든 하위 클래스를 바꿔야 함)
				* 패턴매칭 쓰면 : 
					새 노드 추가하려면 패턴매칭하는 모든 함수에서 새 노드 고려하도록 바꿔야 함
					새 연산 추가는 쉽지(그냥 함수 만들면 되지)
			* 심볼 추출
				``` scala
				def derive(t: Tree, v: String): Tree = t match {
				  case Sum(l, r) => Sum(derive(l, v), derive(r, v))
				  case Var(n) if (v == n) => Const(1)
				  case _ => Const(0)
				}
				```
				* 가드
					* if 키워드 뒤에 오는 표현식
						패턴 매칭에 추가적인 조건 부여
						가드가 거짓이면 패턴 매칭 실패
				* 와일드 카드
					* 모든 값과 매치되고 따로 이름 붙이지 않는다
				``` scala
				def main(args: Array[String]) {
				  val exp: Tree = Sum(Sum(Var("x"),Var("x")),Sum(Const(7),Var("y")))
				  val env: Environment = { case "x" => 5 case "y" => 7 }
				  println("Expression: " + exp)
				  println("Evaluation with x=5, y=7: " + eval(exp, env))
				  println("Derivative relative to x:\n " + derive(exp, "x"))
				  println("Derivative relative to y:\n " + derive(exp, "y"))
				}
				```

* Trait
	* 상속 외에 여러개 코드 불러올 수 있는 방법
	* 코드를 가질 수 있는 인터페이스라고 생각하면 됨!
		* 어떤 class 가 trait 를 상속하면, 그 클래스는 trait 의 interface 를 구현해야만 하고, 동시에 trait 이 가진 모든 코드를 가져오게 됨!
		``` scala
		trait Ord {
		  def < (that: Any): Boolean
		  def <=(that: Any): Boolean =  (this < that) || (this == that)
		  def > (that: Any): Boolean = !(this <= that)
		  def >=(that: Any): Boolean = !(this < that)
		}
		```
			* java 의 comparable 인터페이스와 같은 역할을 함(같다, 같지 않다는 빼고 구현 - 모든 객체에 대해 기본적으로 존재함)
			* 추상함수 사용함
			* any : scala 의 최상위 타입(java 의 object type 과 같음)
		``` scala
		class Date(y: Int, m: Int, d: Int) extends Ord {
		  def year = y
		  def month = m
		  def day = d
		  override def toString(): String = year + "-" + month + "-" + day
		```
			* extends Ord : 트레잇 상속함
		``` scala
		override def equals(that: Any): Boolean =
		  that.isInstanceOf[Date] && {
		    val o = that.asInstanceOf[Date]
		    o.day == day && o.month == month && o.year == year
		  }
		```
			* isInstanceOf : java의 instanceof 와 동일
			* asInstanceOf : java 의 cast 연산자와 동일(호출된 객체가 인자로 들어온 타입의 인스턴스면 그렇게 여겨지도록 변환 / 아니면 ClassCastException)
		``` scala
		def <(that: Any): Boolean = {
		  if (!that.isInstanceOf[Date])
		    error("cannot compare " + that + " and a Date")
		  val o = that.asInstanceOf[Date]
		  (year < o.year) ||
		  (year == o.year && (month < o.month ||
		                     (month == o.month && day < o.day)))
		}
		```
			* error : 주어진 에러 메시지와 함께 예외를 발생 시킴

* Genericity
	* 걍 제네릭
		* ex) 연결 리스트의 원소타입 등
		``` scala
		class Reference[T] {
		  private var contents: T = _
		  def set(value: T) { contents = value }
		  def get: T = contents
		}
		```
			* 클래스 Reference --> type T 에 대해 파라미터 화 돼있음(type T 는 레퍼런스의 원소타입)
			* 변수 초기값이 _ : 기본값을 뜻함(wild card)
				* numeric type 이라면 0, boolean type 이면 false, unit type 이면 (), 모든 객체 타입이면 null
			* 제네릭 쓰고 나면 이 클래스 나중에 쓸 때에 type parameter T 에 미리 적당한 값 넣어줘야한다
		``` scala
		object IntegerReference {
		  def main(args: Array[String]) {
		    val cell = new Reference[Int]
		    cell.set(13)
		    println("Reference contains the half of " + (cell.get * 2))
		  }
		}
		```
			* (cell.get * 2) : get 함수의 리턴 값을 정수처럼 쓸 때에 따로 캐스팅 필요치 않다
			* new Reference[Int] : 정수값만 쓴다고 선언해뒀으니깐 다른 type 을 쓸 수는 없다





https://docs.scala-lang.org/ko/tutorials/scala-for-java-programmers.html 참고후 정리