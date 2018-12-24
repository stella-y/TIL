## Word Piece Model
* tokenizing problem
* 단어를 finite subword unit 으로 표현
* 언어에 상관 없이 모두 적용 가능 / 적용할 언어마다 해당 언어 특징을 반영한 토크나이저를 만들지 않아도 됨
e.g.
```
공연은 끝났어 -> ['공연-' + '-은' + '끝-' + '-났어']
공연을 끝냈어 -> ['공연-' + '-을' + '끝-' + '-냈어']
개막을 해냈어 -> ['개막-' + '-을' + '해-' + '-냈어']
```


### Word piece, units of words
* 
https://lovit.github.io/nlp/2018/04/02/wpm/