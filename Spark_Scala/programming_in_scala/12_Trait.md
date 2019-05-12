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

### Trait 동작 원리
* trait 키워드를 사용하는점을 제외하면 클래스의 정의와 같음
``` scala
trait Philosophical {
	def philosophize()={
		println("I comsume memory, therefore I am!")
	}
}
```
* extends, with 키워드 사용해서 클래스에 조합하여 사용이 가능함
``` scala
//extends 를 이용한 mix in
class Frog extends Philosophical {
	override def toString = "green"
}
```
	* extends 이용시 trait 의 super class 를 암시적으로 상속함
```sh
> val frog=new Frog
frog: Frog=green
> frog.philosophize()
I consume memory, therefore I am!
```
* philosophical 을 type 으로 사용한 경우
```sh
> val phil: Philosophical = frog
phil: Philosophical =green
> phil.philosophize()
I consume memory, therefore I am!
```

