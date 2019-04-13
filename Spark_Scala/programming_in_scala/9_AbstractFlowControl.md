## 9.흐름 제어 추상화
### 1. 코드 중복 줄이기
* 함수를 파라미터로 넘겨서 호출하게 만들 수 있음
```scala
// 중복제거 안한 것
object FileMatcherBefore {                                         // 중복 제거 전 객체
    private def filesHere = (new Java.io.File(".")).listFiles      // 파일 리스트 가져옴
 
    def filesEnding(query: String) = {                             // 파일명이 query로 끝나는 파일들만 리턴 (여기서는 지연 리턴)
        for (file <- filesHere; if file.getName.endsWith(query))
            yield file
    }
 
    def filesContaining(query: String) = {                         // 파일명에 query가 들어가는 파일들만 리턴 (여기서는 지연 리턴)
        for (file <- filesHere; if file.getName.contains(query))
            yield file
    }
 
    def filesRegex(query: String) = {                              // 파일명에 regular expression query와 매칭되는 파일들만 리턴 (여기서는 지연 리턴)
        for (file <- filesHere; if file.getName.matches(query))
            yield file
    }
}

// 중복제거 한 것
object FileMatcherAfter {                                          // 중복 제거 후 객체
    private def filesHere = (new Java.io.File(".")).listFiles      // 파일 리스트 가져옴
 
    def filesMatching(matcher: String => Boolean) = {                         // 파일명이 matcher에 합당하는 파일들만 리턴
        for (file <- filesHere; if matcher(file.getName))
            yield file
    }

    def filesEnding(query: String) = filesMatching(_.endsWith(query))           // 파일의 끝이 query인지 체크하는 클로저 리턴 (클로저의 입력은 파일 이름)
    def filesContaining(query: String) = filesMatching(_.contains(query))       // 파일에 query가 들어가있는지 체크하는 클로저 리턴
    def filesRegex(query: String) = filesMatching(_.matches(query))             // 파일이름이 query regular expression 에 매칭되는지 체크하는 클로저 리턴
}
```
* FileMatcherBefore 부분에서 일일이 함수를 다 새로 씀
* FileMatcherAfter 의 filesMatching 함수를 파라미터로 받을 수 있는 형태로 선언해 둠(matcher라는 변수명으로)
* FileMatcherAfter 의 filesEnding, filesContaining, filesRegex 의 함수를 선언할때 filesMatching 을 이용하게 됨
	* filesMatching(\_.endsWith(query)) 는 file 이름이 query 로 끝나는지 체크하는 클로저를 리턴함
		* filesMatching 에서 인자가 뭐가 들어갈지 모른다는 의미로 \_ 를 씀(\_.endsWith 등)

### 2. 코드 단순화
```scala
// 코드 단순화 전
def containsNeg(nums: List[Int]):Boolean = {                          // nums 리스트 내부에 음수가 존재하는지 체크
    var exists = false
    for (num <- nums)
        if (num < 0)
            exists = true
    exists
}
 
def containsOdd(nums: List[Int]): Boolean = {                         // nums 리스트 내부에 홀수가 존재하는지 체크
    var exists = false
    for (num <- nums)
        if (num % 2 == 1)
            exists = true
    exists
}

// 코드 단순화 후
def containsNegSimple(nums: List[Int]):Boolean = nums.exists(_ < 0)        // containsNeg와 동일한 함수
def containsOddSimple(nums: List[Int]):Boolean = nums.exists(_ % 2 == 1)   // containsOdd와 동일한 함수
```
* scala 의 List 에 있는 exists 함수는 함수 파라미터를 받을 수 있게 설계 돼 있음
* exists 호출할 때에 인자로 (\_ < 0), (\_ % 2 == 1) 등의 함수를 받을 수 있는 것

### 3. 커링(Curring)
* 인자 목록을 여러개 가지고 있게 선언
* 인자 목록 개수만큼 중첩된 함수가 존재하고, 인자를 모두 입력하여 호출시 이를 모두 호출하는 형태
* 따라서 일부 인자만 채워주면 나머지 인자를 채울 수 있는 함수가 리턴
```scala
def plainOldSum(x: Int, y: Int) = x + y        // 일반적인 형태의 덧셈 함수
val res1 = plandOldSum(1, 2)
 
def curriedSum(x: Int)(y: Int) = x + y         // 커링을 사용한 덧셈 함수
val res2 = curriedSum(1)(2)
 
def first(x: Int) = (y: Int) => x + y          // 클로저를 사용한 덧셈 함수
val second = first(1)
val res3 = second(2)
 
val onePlus = curriedSum(1) _                  // 커링을 사용하면 클로저를 사용해서 동작하는 것과 동일하게 사용할 수 있음
val res4 = onePlus(2)                          // 실제 내부적으로는 클로저를 사용하는 동작과 동일한 바이트코드가 생성됨
```
* curring 으로 선언된 함수의 경우 인자를 다 넣고 호출하지 않을 경우 값을 리턴하지 않고, 나머지 인자를 후에 받을 수 있는 함수 형태를 리턴하게 됨

### 4. 새로운 제어구조
```scala
def twice(op: Double => Double, x: Double) = op(op(x))     // x에다가 op를 두번 연산하고 결과값을 리턴해주는 함수
val res = twice(_ + 1, 5)                                  // res에는 7이 저장됨
```
* loan pattern(빌려주기 패턴)
```scala
def withPrintWriter(file: File, op: PrintWriter => Unit) = {         // 결과를 저장할 파일과, writer에서 호출할 함수 형태를 전달해줌
    val writer = new PrintWriter(file)
    try {
        op(writer)
    } finally {
        writer.close()
    }
}
withPrintWriter(new File("date.txt"), w => w.println(new java.util.Date))
 
 
/*
date.txt 에 println(new java.util.Date) 의 결과가 저장됨 (현재 날짜 시간 저장)
동작 과정은
val op = (w: PrintWriter): Unit = w.println(new java.util.Date)
를 생성하고 이걸 인자로 넘겨줌
그리고 내부에서 op의 파라미터라 writer를 넘겨줘서 실제로 생행되는건 writer.println(new java.util.Date) 임
 
여기서 withPrintWriter가 파일을 닫고있음
따라서 외부에서는 withPrintWriter 한테 File 자원을 빌려주고 닫는건 신경쓰지 않아도 됨
*/
```
* parameter 가 1개인 경우 소괄호를 중괄호로 대체 가능 --> 내장제어구문인것처럼 사용하는게 가능해진다
```scala
def withPrintWriter(file: File)(op: PrintWriter => Unit) = {         // 위와 동일하지만 커링 사용
    val writer = new PrintWriter(file)
    try {
        op(writer)
    } finally {
        writer.close()
    }
}
val file = new File("date.txt")
withPrintWriter(file) {
    writer => writer.println(new java.util.Date)                     // 요렇게 중괄호를 사용해서 내장 구문인것처럼 쓸 수 있음. 뭐가 좋은진 모르겠음
}
```

### 5. 이름에 의한 호출 파라미터
* Call by name 방식
```scala
var assertOn = True
def byNameAsssert(predicate: => Boolean) = {        // by-name parameter를 사용
    if (assertOn && !predicate)
        throw new AssertionError
}
def boolAsssert(predicate: Boolean) = {             // 단순히 파라미터를 전달 - 동일하게 동작하나 lazy evaluation이 동작하지 않음
    if (assertOn && !predicate)
        throw new AssertionError
}
 
byNameAsssert(5 > 3)             // 정상 동작
boolAsssert(5 > 3)               // 정상 동작
byNameAsssert(x / 0 == 0)        // division by zero 발생
boolAsssert(5 > 3)               // division by zero 발생

assertOn = False
byNameAsssert(x / 0 == 0)        // 정상동작 (x / 0 연산이 일어나지 않은채로 전달)
boolAsssert(5 > 3)               // division by zero 발생
```

