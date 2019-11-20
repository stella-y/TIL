## [암시적 변환과 암시적 파라미터]
다른 라이브러리 가져와서 바꾸거나 확장해서 쓰고싶은 경우, 다른언어(루비 : module / smalltalk : package 들에서 서로 class 추가하는게 가능 / c# : static extension method) 이를 함부로 변환하면 추후 다른 부분에서 문제가 생길 수 있음
스칼라에서는 이걸 암시적 변환, 암시적 파라미터로 해결한다.

### 21.1 암시적 변환
* 암시적 변환 - 서로를 고려하지 않고 독립적으로 개발된 두 덩어리의 소프트웨어를 한데 묶는데 유용함
	* 근본적으로 동일한 어떤 대상을 각 라이브러리가 각각 다르게 인코딩할 수 있음
	* 한 타입을 다른 타입으로 변경하는데 필요한 명시적 변환의 숫자를 줄일 수 있음
* 아래예시는 java 에서의 swing활용 예
	* swing : os event 를 처리해, 플랫폼에 독립적엔 event obj로 바꾸고, 이런 event 들을 event listener 라는 이름의 어플리케이션 구성요소로 전달함
* java 에서 개발했다면 아래와 같을 것
```java
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JOptionPane;

public class ActionExam implements ActionListener{ 
	JButton btn1 = new JButton("클릭1"); //버튼 생성
	JButton btn2 = new JButton("클릭2"); //버튼 생성
	public ActionExam() //생성자
	{
		// 레이아웃 설정
		this.setLayout(new FlowLayout());

		// 버튼 추가
		this.add(btn1);
		this.add(btn2);

		// 크기 및 보기 설정
		this.setSize(300, 200);
		this.setVisible(true);

		// 이벤트 등록하기
		btn1.addActionListener(this);
		btn2.addActionListener(this);
	}
	public static void main(String[] args)
	{
		// 실행
		new ActionExam();
	}

	@Override
	public void actionPerformed(ActionEvent e)
	{
		//액션 리스너 재정의
		if (e.getSource().equals(btn1))
		{
			JOptionPane.showMessageDialog(this, "1번 버튼 눌렀네");
		}
		else
		{
			JOptionPane.showMessageDialog(this, "2번 버튼 눌렀네");
		}
	}
}
```
[참고: https://programmingsummaries.tistory.com/62 ]

* 위와 같은 형식을 스칼라에서 적용하면 아래와 같을 것
```scala
val button = new JButton
button.addActionListener(
	new ActionListener{
		def actionPerformed(event: ActionEvent){
			println("pressed!")
		}
	}
)
```
	* 그런데 이때에 준비과정을 위한 코드가 너무 많다는게 책에서의 주장...
		* (리스너가 ActionListener인 것/ 콜백 메소드가 actionPerformed 라는 것/ 리스너 추가 함수에 전달할 인자가 action event 인 것)
		* addActionListener 에 전달할 인자라면 당연한 것이므로, 위의 세가지는 다 필요없는 정보.
		* 정말 새로운 정보는 println 뿐이다.
* 스칼라에서는 암시적 변환을 이용하여 아래와 같이 핵심 정보만 포함하고도 동작하게 하고싶음
```scala
button.addActionListener( //타입 불일치(이대신 actionListner 를 반환해야함)
	(_: ActionEvent) => println("pressed!")
)
//(스칼라 2.12 에서는 이 코드가 동작함)
```

* 타입에러를 막기 위해 두 타입 사이의 암시적 변환 방법을 작성 (함수를 액션 리스너로 바꾸기)
```scala
implicit def function2ActionListener(f: ActionEvent => Unit) =
	new ActionListener {
		def actionPerformed(event: ActionEvent) = f(event)
	}
	//유일한 인자로 함수를 받아서 action listner 를 반환
```
* 이러면 아래와 같이 동작이 가능하고, 
```scala
button.addActionListener(
	function2ActionListener(
		(_: ActionEvent) => println("pressed!")
	)
)
```
* 위에서 function2ActionListener 에 implicit 해줬으니 이제 위에서 시도했던 아래 코드도 동작함
```scala
button.addActionListener(
	(_: ActionEvent) => println("pressed!")
)
```
	* 위코드 동작방식
		* 컴파일러는 코드를 그대로 컴파일 시도 -> 타입오류 발생 -> 암시적변환으로 문제 해결 가능한지 확인 -> function2ActionListener 가 있으니 이걸로 시도해본다 -> 작동하면 계속 다음단계를 진행한다...

### 21.2 암시 규칙
* 암시적 정의 : 컴파일러가 타입 오류를 고치기 위해 삽입할 수 있는 정의들
	* e.g. x+y 라는 표현식에 타입오류가 있다면 컴파일러는 convert(x)+y 를 시도할 것
	* 여기서의 convert 는 사용 가능한 암시적 변환 중 하나가 된다
	(convert 가 x 를 + 메소드를 가진 어떤것으로 변환할 수 있다면 그 변환이 문제를 해결해서 타입 검사를 통과하고 제대로 실행될 수 있는 것)
	* convert 가 실제로 간단히 변환 함수에 지나지 않다면, 이를 소스코드에서 빼는게 오히려 코드를 더 명확하게 하는 일일 수 있다(는게 책에서의 주장...)

#### 컴파일러가 암시적 변환을 처리하는 일반 규칙
1. 표시규칙 : implicit 로 표시한 정의만 검토대상이다
	* 변수, 함수, 객체 정의에 implicit 표시를 달 수 있음
	* e.g. implicit def intToString(x: Int) = x.toString
	* 컴파일러가 x+y 를 convert(x)+y로 바꾸는 경우는 convert 가 implicit로 표시된 경우 뿐인 것
	* 스코프 안에 있는 임의의 함수를 선택해 '변환함수'로 사용하는 경우를 방지하기 위한 것...(암시적이라고 명시한 것 중에서만 찾게 됨)
2. scope 규칙 : 삽입된 implicit 변환은 scope 내에서 단일 식별자로만 존재하거나, 변환의 결과나 원래 타입과 연관이 있어야한다.
	* '단일식별자' - someVariable.convert 이런 형태가 아닌 하나
	(위의 경로에서 가져오고 싶다면 저 경로 자체를 import 해서 단일식별자로 가져올 수 있게 해야한다)
	* 단일 식별자 규칙에서의 예외 - 컴파일러는 원 타입이나 변환 결과 타입의 동반 객체에 있는 암시적 정의도 살펴본다
```scala
object Dollar {
	implicit def dollarToEuro(x: Dollar): Euro = ...
}
class Dollar { ... }
```
		* 










