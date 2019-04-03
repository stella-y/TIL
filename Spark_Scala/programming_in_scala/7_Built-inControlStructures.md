## 7.Built-in Control Structures(내장제어구문)
* if, while, for, try, match
* scala 는 함수형 언어 --> if, for, try, match 모두 결과로 값을 내 놓는다

### 7.1 if 표현식
* Imperative programming(명령형)
```scala
var filename="default.txt"
if (!args.isEmpty)
	filename=args(0)
```
* 위의 표현을 축약 가능(스칼라의 if 는 값을 내놓기 때문)
* 덧붙여, var 대신 val 을 쓸 수 있게 됨(동일성 추론)
```scala
val filename=
	if(!args.isEmpty) args(0)
	else "default.txt"
```
* 부수 효과가 없다고 가정하면, 변수명을 표현식으로 대체할 수 있음
```scala
//print(filename)
println(if (!args.isEmpty) args(0) else "default.txt")
```

### 7.2 while loop
* while, do-while은 수행 결과가 관심을 가질만한 값이 아니기 때문에 표현식이라 하지 않고 '루프'라고만 부름
* 결과 타입 :  Unit / ()로 표기함
	* procedure 에서의 return 값도 unit
```scala
def greet()={println("hi")}
()==greet()
//hi
//res0: Boolean=true
```
* 스칼라에서 할당의 결과는 항상 unit
```scala
var line=""
while((line=readLine())!="") //--> 항상 참이된다!
	println("Read: "+line)
```
	* java 에서의 할당결과가 할당값인 반면, 스칼라에서의 할당 결과는 유닛값()
	* line=readLine()의 결과는 항상 () --> 조건 식부분이 거짓이 될 수가 없다!
* 순수 함수형 언어는 while 을 쓰지 않음(return 값이 없으니까!) --> 근데 재귀로만 대체하면 가독성이 너무 떨어져서 쓰게 해주는것 뿐임
	* --> while 은 최대한 적게 쓰는걸 권장함(결과를 내지 않기때문에 변화를 주려면 i/o 나 var 를 쓸 수밖에 없기때문...)

### 7.3 for loop
* **반복 처리를 위한 스위스 만능칼** --> 책에서의 표현...

#### Collection Iteration
* collection 에 있는 모든 요소를 iteration
```scala
var filesHear=(new java.io.File(".")).listFiles
for (file <- filesHere)
	println(file)
```
* file <- filesHere
	* Generator / 각 반복 단계마다 file 이란 새로운 val 을 각 원소의 값으로 초기화 함
	* filesHere 가 Array[File]타입 --> file 은 File 타입임을 추론 가능
* array 뿐 아니라, 어떤 종류의 컬렉션에서도 동작함
	* range (i <- 1 to 4), (i <- 1 until 4)

#### filtering
* collection 내의 모든 원소를 iteration 하고 싶지 않은 경우 --> for 표현식에 filter 를 추가
```scala
val filesHere=(new java.io.File(".").listFiles)
for (file <- filesHere if file.getName.endsWith(".scala"))
	println(file)
```
* **for 문의 결과값은 <- 절에 의해 타입이 정해지는 collection**
```scala
//필터 여러개 추가
for (
	file <- filesHere
	if file.isFile
	if file.getName.endsWith(".scala")
) println(file)
```

#### nested iteration
* 여러개의 <- 추가해서 nested loop 작성 가능
```scala
def fileLines(file: java.io.File)=scala.io.Source.fromFile(file).getLines().toList

def grep(pattern: String)=
	for (
		file <- filesHere //generator
		if file.getName.endsWith(".scala"); //filter
		line <- fileLines(file) //generator
		if line.trim.matches(pattern) //filter
		) println(file+ ": "+line.trim)
grep(".*gcd.*")
```
* 만약 () 대신 {} 쓴다면 세미콜론 생략 가능(세미콜론 추론 규칙 --> 괄호, 대괄호 내부에선 세미콜론 추론하지 않음)

#### for 중에 변수 binding
* for 중에서 한번만 계산하고 싶은 부분은 등호 이용해 새로운 변수에 결과 할당해둘 수 있음
* 이때 val 라는 키워드를 사용하지 않는다
```scala
//위의 예제에서 line.trim 의 표현 반복을 제거한 것
def grep(pattern: String)=
	for {
		file <- filesHere
		if file.getName.endsWith(".scala")
		line <- fileLines(file)
		trimmed=line.trim
		if trimmed.matches(pattern)
	} println(file + ": "+ trimmed)
grep(".*gcd.*")
```

#### 새로운 collection 생성
* iteration 의 매 반복 단계의 결과를 저장하기 위한 값을 만들 수 있다!
* for 표현식의 본문 **앞**에 yield 키워드 사용
	* 결과값이라 꼭 마지막에 와야할 것 같은 느낌이 들지만 아니란걸 유의할 것
	* for 의 본문의 iteration 마다 만들어내는 결과값을 모은단 걸 기억할 것
```scala
val filesHere=(new java.io.File(".").listFiles)

def scalaFiles=
	for{
		file <- filesHere
		if file.getName.endsWith(".scala")
	} yield file

//아래는 틀린 표현
for (file <-filesHear if file.getName.endsWith(".scala")){
	yield file
}
//yield 는 위 코드의 중괄호 앞에 위치해야 함
```
* for 표현식의 본문을 수행할때마다 값(위 코드에선 file)을 하나씩 만들어 냄
* 위 코드에서 전체 결과는 Array[File]

### 7.4 Try 표현식 다루기

#### 예외 발생시키기
* 방법은 자바와 같음
```scala
throw new IllegalArgumentException //
```
* throw --> 스칼라에선 얘도 결과값이 있음 : Nothing type
	* 예외 발생시 결과값을 돌려주기도 전에 제어 흐름이 호출한 쪽으로 넘어감(결과값을 실제로 써먹는 경우는 없는 것)
	* if 문의 코드 분기는 모두 표현식이어야 하므로, throw 만 특별취급하면 문법구조나 컴파일러 처리가 복잡할 것이기때문

#### 발생한 예외 잡기
```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

try {
	val f = new FileReader("input.txt")
} catch{
	case ex: FileNotFoundException => //파일을 못 찾는 경우 처리
	case ex: IOException => // 그 밖의 IO 오류 처리
}
```
* 패턴 매치와 일관성 위해서 위와 같은 형식 차용한 것 --> 15장에 더 있다고함

#### finally 절
* 표현식의 결과가 어떻든 특정 코드를 반드시 수행하고 싶을 때(java 랑 같음)
```scala
import java.io.FileReader

val file=new FileReader("input.txt")
try {
	//파일을 사용한다
} finally{
	file.close()//파일을 닫는다
}
```

#### 값 만들어내기
```scala
import java.net.URL
import java.net.MalformedURLException

def urlFor(path: String)=
	try {
		new URL(path)
	} catch {
		case e: MapformedURLException =>
			new URL("http://www.scala-lang.org")
	}
```
* try-catch-finally 도 값을 return
* 위의 예시에서
	* 예외가 발생하지 않으면 전체 결과는 try 절의 수행 결과
	* 예외 발생했는데 처리 못하면 표현식의 결과는 전혀 없음
		* finally 절에 결과값이 있대도 버려짐
* java 와 비교
	* java : finally 안에서 명시적으로 return 을 사용하거나, 예외 발생시키면 try 블록이나 catch 절에서 발생한 원래의 결과물을 덮어씀
* **finally 에서는 값을 반환하지 않는게 최선이다!!**
* 파일을 닫거나 정리하는 작업 등의 부수 효과에 사용
```scala
def f(): Int = try return 1 finally return 2 // 결과 =2
def g(): Int = try 1 finally 2 //결과 = 1
```


### 7.5 Match 표현식
* switch 와 유사
```scala
val firstArg=if (args.length > 0) args(0) else ""
val friend=
	firstArg match {
		case "salt" => "pepper"
		case "chips" => "salsa"
		case "eggs" => "bacon"
		case _ => "huh?" // _ : default (스칼라에서는 완전히 알려지지 않은값 표시를 위한 위치 표시자(placeholder)로 종종 이용함)
	}
```
* Java 의 switch 와의 차이
	* case 문에서의 대상이 다름
		* java 에서는 case 문에 enum, 정수 타입의 값, 문자열 만 쓸수 있음
		* scala 에서는 어떤 종류의 상수도 사용 가능
	* break 문이 없음
		* case 문 마다 break 가 암묵적으로 있어서 break 가 없어도 다음으로 넘어가지 않음
	* match 엔 결과값이 있음
		* 위의 코드에선 match의 결과가 friend 의 값으로 저장될 것

### 7.6 break 와 continue 문 없이 살기
* scala 에선 break 와 continue 가 없다!(함수리터럴과 어울리지 않는단다...)
* continue 문을 if 로 break 문을 boolean 변수로 대체하면 된다
```java
int i=0;
boolean foundIt=false;
while(i < args.length){
	if (args[i].startsWith("-")){
		i = i + 1;
		continue;
	}
	if (args[i].endsWith(".scala")){
		foundIt = true;
		break;
	}
	i = i + 1;
}
```
* java code 를 scala code 로 변형(break, continue 제거)
```scala
var i = 0
var foundIt = false
while( i < args.length && !foundIt){
	if (!args(i).startsWith("-")){
		if (args(i).endsWith(".scala"))
			foundIt = true
	}
	i = i + 1
}
```
* var 대신 val 사용 위해 재귀로 변환
```scala
def searchFrom(i: Int): Int =
	if (i >= args.length) -1
	else if (args(i).startsWith("-")) searchFrom(i + 1)
	else if (args(i).endsWith(".scala")) i
	else searchFrom(i + 1)
val i = searchFrom(0)
```
* 굳이 break 를 쓰고 싶다면 스칼라 표준 라이브러리에 있음
```scala
import scala.util.control.Breaks._
import java.io._

val in = new BufferedReader(new InputStreamReader(System.in))

breakable {
	while (true) {
		println("? ")
		if (in.readLine() == "") break
	}
}
```

### 7.7 변수 스코프
* java 에서와 동일하다


### 7.8 명령형 스타일 코드 리팩토링



