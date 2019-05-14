##12.Trait
### overview
* 스칼라에서 트레이트는 코드 재사용의 근간을 이루는 단위
	* 트레이트로 메소드, 필드 정의를 캡슐화 하면 트레이트를 조합한 클래스에서 그 메소드나 필드를 재사용할 수 있음
* 상속 - 하나의 부모만 갖는다 / 트레이트는 몇개든 혼합사용(mix in)할 수 있다.
* 이번장에서 할 것
	* 트레이트를 써먹는 가장 일반적인 방법 두가지
		1. thin interface 를 확장해 rich interface 만들기
		2. 쌓을 수 있는 변경(Stackable modification) 정의
	* + ordered trait 사용법 + 다른 언어에서의 다중상속과의 차이점

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
```sh
> val phil: Philosophical = frog
phil: Philosophical =green
> phil.philosophize()
I consume memory, therefore I am!
```
	* phil 변수의 타입은 Philosophical 트레이트 --> phil 변수를 Philosophical trait 를 mix in 한 어떤 객체로도 초기화시킬 수 있음
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
	override def toString="gree"
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














