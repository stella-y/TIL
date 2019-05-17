## 12.Trait
### overview
* 스칼라에서 트레이트는 코드 재사용의 근간을 이루는 단위
	* 트레이트로 메소드, 필드 정의를 캡슐화 하면 트레이트를 조합한 클래스에서 그 메소드나 필드를 재사용할 수 있음
* 상속 - 하나의 부모만 갖는다 / 트레이트는 몇개든 혼합사용(mix in)할 수 있다.
* 이번장에서 할 것
	* 트레이트를 써먹는 가장 일반적인 방법 두가지
		1. thin interface 를 확장해 rich interface 만들기
		2. 쌓을 수 있는 변경(Stackable modification) 정의
	* \+ ordered trait 사용법 + 다른 언어에서의 다중상속과의 차이점

### 12.1 Trait 동작 원리
1. trait 키워드를 사용하는점을 제외하면 클래스의 정의와 같음
``` scala
trait Philosophical {
	def philosophize()={
		println("I comsume memory, therefore I am!")
	}
}
```
2. extends, with 키워드 사용해서 클래스에 조합하여 사용이 가능함
``` scala
//extends 를 이용한 mix in
class Frog extends Philosophical {
	override def toString = "green"
}
```
3. trait 도 AnyRef 의 자식 class 임
	* extends 이용시 trait 의 super class(아래에서 Philosophical 의 super class 는 AnyRef) 를 암시적으로 상속함
```sh
> val frog=new Frog
frog: Frog=green
> frog.philosophize()
I consume memory, therefore I am!
```
4. trait 도 type 을 정의함
	* phil 변수의 타입은 Philosophical 트레이트 --> phil 변수를 Philosophical trait 를 mix in 한 어떤 객체로도 초기화시킬 수 있음
```sh
> val phil: Philosophical = frog
phil: Philosophical =green
> phil.philosophize()
I consume memory, therefore I am!
```

5. with 을 활용해서 여러 trait 를 mix in 하는게 가능하다
```scala
class Animal
trait HasLegs
class Frog extends Animal with Philosophical with HasLegs{
	override def toString="green"
}
```
6. trait 에서 정의된 method 를 override 하는게 가능하다
```scala
class Animal
class Frog extends Animal with Philosophical{
	override def toString="green"
	override def philosophize() = {
		println("It ain't easy being "+toString+"!")
	}
}
```
```sh
> val phrog: Philosophical = new Frog
phrog: Philosophical = green
> phrog.philosophize()
It ain't easy being geen
```
* method 구현이 들어간 interface 처럼 보이지만, trait 는 그 이상의 것이다!(책에서 이렇게 썼음...)
	* field 선언해서 상태를 유지할 수 있다. --> trait 를 정의할 때 class 정의하면서 할 수 있는건 다 할 수 있음!
	* 문법도 두가지 경우를 제외하면 완벽히 동일함
		1. trait 는 class parameter 를 가질 수 없음
			e.g. trait NoPoint(x:Int, y: Int) 이런게 불가능함
		2. super 호출을 동적으로 바인딩함(class 에서는 정적으로 바인딩)
			* 여러 method overriding 할 때에, class 구현에 mix in 할때마다 method 구현이 달라짐
			* --> stackable modification 이 가능해짐

### 12.2 간결한 인터페이스와 풍부한 인터페이스(Thin interface and Rich interface)
* trait 의 주된 활용 방식 - 어떤 클래스에 그 클래스가 이미 갖고 있는 메소드를 기반으로 하는 새로운 메소드 추가
(thin interface to rich interface)
* 자바의 interface 는 기본적으로 thin 함 / 구현하는 class 에서 정의해야할게 많음
* trait 는 rich 한 interface 를 구현하기가 더 좋음

### 12.3 예제

### 12.4 Ordered trait
* compare 함수만 구현하면, 연산자에 대한 함수를 제공함
* ordered trait 가 없다면 분수의 비교 연산을 아래와 같이 구현해야 했을 것임
```scala
class Rational(n: Int, d: Int){
	//...
	def < (that: Rational) = this.numer * that.denom < that.numer * this.denom
	def > (that: Rational) = that < this
	def <= (that: Rational) = (this > that) || (this == that)
	def >= (that: Rational) = (this > that) || (this == that)
}
```
* ordered trait 를 이용한다면!
```scala
class Rational(n: Int, d: Int) extends Ordered[Rational]{
	//...
	def compare(that: Rational)=(this.numer * that.denom) - (that.numer * this.demon)
}
```
* ordered trait 이용할 때에 할 일 두 가지
	1. 다른 trait 와 달리 type parameter 를 명시해야함
	2. compare method 를 정의한다
		* 두 객체가 동일하면 0, 호출 대상 객체 자신이 인자보다 작으면 음수, 더 크면 음수를 반환해야 함
* 이때 ordered trait 가 equals 를 정의하지는 않음!!
	* 정의가 불가능하기 때문임
	* 비교 관점에서 equals 를 구현하려면 객체 타입을 알아야 하기때문에 타입소거(type erasure) 때문에 이게 불가능하다고 함. (이걸 우회할 방법은 30장에 나옴)
		* type erasure
			* 자바 컴파일러에서 type 검사하고 나서 byte code 를 만들면서 타입 관련 정보를 제거함
				* ArrayList<Integer> 를 instance 화 한 객체와 ArrayList<Float> 을 instance 환 객체의 클래스를 실행 시점에 getClass() 등을 사용해보면 같다고 나옴
				* e.g. List(1,2,3).getClass()==List('a', 'b').getClass()

### 12.5 Trait 를 이용해 변경 쌓아올리기
* 예시
	* put, get method 가 있는 정수 queue class 를 가정
	* queue class 를 변경하는 trait 세 개 정의
		* doubling : 모든 정수를 두배로
		* incrementing : 모든 정수에 1을 더한다
		* filtering : 음수를 걸러낸다
```scala
abstract class IntQueue{
	def get(): Int
	def put(x: Int)
}
```
```scala
import scala.collection.mutable.ArrayBuffer
class BasicIntQueue extends IntQueue{
	private val buf = new ArrayBuffer[Int]
	def get() = buf.remove(0)
	def put(x: Int) = { buf += x}
}
```
``` scala
//doubling trait
trait Doubling extends IntQueue {
	abstract override def put (x: Int)={ super.put(2 * x) }
}
```
* 위와 같이 extends IntQueue 를 하면, IntQueue 를 상속받는 클래스에서만 Doubling trait 를 사용할 수 있음
* 위와 같이 abstract method가 super를 호출
	* 일반적인 클래스라면 이런식으로 호출할 경우 실행 시점에 호출에 실패할게 뻔해서 이걸 금지함
	* trait 의 경우 성공할 수 있음
	* 호출을 동적으로 바인딩하기 때문에, doubling 을 put 을 제공하는 trait 나 class 에 mixin 하면 doubling trait 에서 super.put 을 호출해도 아무 문제가 없음
	* abstract override - 컴파일러에게 의도적으로 super 의 메소드를 호출했다는 사실을 알려줌
		* 클래스에는 사용할 수 없음
		* abstract override 메소드가 어떤 트레이트에 있다면, 그 트레이트는 반드시 abstract override 가 붙은 메소드를 구현하는 클래스에 mix in해야함
```sh
> class MyQueue extends BasicIntQueue with Doubling # basic~ 을 상속받고, doubling 을 구현함
defined class MyQueue
> val queue = new MyQueue
queue: MyQueue= MyQueue@44bbf788
> queue.put(10)
> queue.get()
res12: Int = 20
```
(위에서 MyQueue 클래스엔 아무것도 구현 안해도, trait mix in 만으로 이게 다 가능하다)
* BasicIntQueue with Doubling 을 바로 new 와 함께 사용하는것도 가능함
	* e.g.val queue=new BasicIntQueue with Doubling
```scala
trait Incrementing extends IntQueue {
	abstract override def put(x: Int) = { super.put(x + 1)}
}
trait Filtering extends IntQueue {
	abstract override def put(x: Int) = {
		if(x >= 0) super.put(x)
	}
}
```
```sh
> val queue= (new BasicIntQueue with Incrementing with Filtering)
queue: BasicIntQueue with Incrementing with Filtering
> queue.put(-1); queue.put(0); queue.put(1)
> queue.get()
res15: Int = 1
> queue.get()
res16: Int = 2
```
* mix in 은 순서가 중요함
	* 가장 오른쪽에 있는 trait 효과를 가장 먼저 호출
```sh
# mix in 순서 바꿔보기
> val queue = (new BasicIntQueue with Filtering with Incrementing)
queue: BasicIntQueue with Filtering with Incrementing
> queue.put(-1); queue.put(0); queue.put(1)
> queue.get()
res17: Int = 0
> queue.get()
res18: Int = 1
> queue.get()
res19: Int = 2
```

### 12.6 왜 다중상속은 안되는가
* 다중 상속 언어에서 super 호출시엔 어떤 메소드를 부를지에대한 결정은 호출이 이뤄지는 곳(컴파일 타임)에서 함
* 트레이트를 사용할때는 특정 클래스에 믹스인한 클래스와 트레이트를 선형화해서 어떤 메소드를 호출할지 결정
```scala
val q = new BasicIntQueue with Incrementing with Doubling
q.put(42)
```
* 위 코드를 상속이라고 상상한다면 q.put(42)에서 42를 두배한 후 put 하고 끝날 것(trait 처럼 incrementing 하지 못함)
	* 이 때에 각 코드는 super class 의 put 을 따로 호출하지, 1증가시기키고 두배하는 형태로 동작하지 않음
``` scala
trait MyQueue extends BasicIntQueue with Incrementing with Doubling {
	def put(x: Int) = {
		Incrementing.super.put(x) // 스칼라코드 아님 (다중 상속이라 이해해보는 것)
		Doubling.super.put(x)
	}
}
```

* trait 는 선형화로 이 문제를 해결하고 있음
	* 클래스를 instance 화 할때, 클래스 자기자신, 조상클래스, 믹스인 트레이트를 한줄로 세워서 순서를 정함(맨앞이 자기자신)
	* super 를 여기서 호출하면 해당 순서에서 한단계 다음에 있는 method 가 호출되는 것
	* 마지막에 있는 클래스(최상위 클래스)가 아닌 모든 메소드에서 super 를 호출하면 결과적으로 여러 동작을 쌓아올리게 되는 것


### 12.7 트레이트냐 아니냐, 이것이 문제로다(책에 이렇게 돼있음)
* 트레이트를 쓸지, 추상 클래스를 쓸지 결정 가이드라인
	1. 재사용하지 않는다 - class
	2. 서로 관련없는 클래스에서 여러 행위를 여러번 재사용 - trait
	(클래스 계층의 각기 다른 부분에 믹스인 할 수 있는건 trait 뿐)
	3. 스칼라에서 정의한 내용을 자바코드에서 상속해야한다 - class
	4. 컴파일한 바이너리 형태로 배포할 예정이고, 누군가 이걸 상속해서 쓸 것 같다 - class
	5. 위의 사항을 다 고려했는데 모르겠다 - trait!(이게 더 좋으니까!)




