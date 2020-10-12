1. 반복가능한 객체
	- 요소가 여러개 들어있고, 한번에 하나씩 꺼낼 수 있는 객체(e.g. 문자열, 리스트, 딕셔너리, 세트)
	- 객체에 _iter_ 메서드가 있는지 확인해보면 됨 (dir(객체))
```python
# list
>>> it = [1, 2, 3].__iter__()
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    it.__next__()
StopIteration

# 문자열
>>> 'Hello, world!'.__iter__()
<str_iterator object at 0x03616770>
>>> {'a': 1, 'b': 2}.__iter__()
<dict_keyiterator object at 0x03870B10>
>>> {1, 2, 3}.__iter__()
<set_iterator object at 0x03878418>

# 눈에 보이지 않는 반복 가능한 객체
>>> it = range(3).__iter__()
>>> it.__next__()
0
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    it.__next__()
StopIteration
``` 

2. for 문의 비밀
```python
for i in range(3): # 이 부분에서!
	print(i)
```
	- range에서 \_iter\_ 로 iterator 얻고, 반복시마다 iterator 에서 \_next\_로 숫자 꺼내서 i 에 저장 -> iteration이 끝나면 반복도 끝

3. iterable 과 iterator 구분
- iterable에서 \_iter\_ 메소드를 호출해서 iterator를 얻는 것!

4. sequence 객체와의 차이
시퀀스 객체 = [list, tuple, range, str\](요소의 순서가 정해져있는 객체)
반복 가능한 객체 = 시퀀스 객체 + [dict, set]

5. iterator 만들기
```python
#iterator.py
class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')
```
6. index 로 접근할 수 있는 iterator 만들기
```python
class Counter:
    def __init__(self, stop):
        self.stop = stop
 
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
 
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
```

7. iter, next 함수
- iter는 객체의 __iter__ 메서드를 호출해주고, next는 객체의 __next__ 메서드를 호출해줌
- iter
	- 반복을 끝낼 값을 지정하면 특정 값이 나올때에 반복을 바로 끝냄
	- 이 경우 반복 가능한 객체 대신 호출 가능한 객체(callable)를 넣어줌
	- e.g. iter(호출가능한 객체, 반복을 끝낼 값)
```python
import random
it=iter(lambda : random.randint(0,2), 2) # 호출 가능한 객체 넣어야하니깐 함수 or 람다 넣어야
next(it) #0
next(it) #3
next(it) #2
next(it) #--> 이건 exception!
```
- next
	- 반복할 수 있으면 해당값 출력, 끝나면 기본값 출력(stop iteration출력 x)
	
참고 : https://dojang.io/mod/page/view.php?id=2405


