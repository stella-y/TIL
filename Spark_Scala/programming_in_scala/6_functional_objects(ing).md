## 함수형 객체
### 스칼라에서의 클래스 작성법
* 기본
```scala
class Rational(n:Int, d:Int)            // class 정의에 기본 파라미터 및 기본 생성자 자동 생성 (private로 저장됨)

class Rational(n:Int, d:Int) {          // class 내부에 있지만 필드나 메소드 정의에 없는 코드는 기본 생성자에 자동 포함
    println("Created " + n + "/" + d)
}
```
* toString method override
	* java.lang.Object 클래스의 toString
		* 클래스 이름, @표시, 16진수 숫자 출력함
		* 디버그 출력문, 로그 메시지, 테스트 실패보고, 인터프리터 디버거 출력시 정보 제공해서 도움을 주기 위한 것
		* 디폴트 값 자체는 별로 도움이 안돼서, override 해서 값을 변환해주면 더 좋음
```scala
class Rational(n:Int, d:Int){
	override def toString=n+"/"+d
}
```
* 선결 조건 지정
	* assert 같은 역할 --> require 사용
```scala
class Rational(n:Int, d:Int) {
    require(d != 0)                         // require를 통해 선결조건 전달 -> 실패시 IllegalArgumentException
    override def toString = n + "/" + d
}
```
