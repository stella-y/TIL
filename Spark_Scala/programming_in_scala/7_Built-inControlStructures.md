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

def grep(patter: String)=
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
* 
















