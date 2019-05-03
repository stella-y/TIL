## python 에서 url encoding 하는 법
### encodeurlencode()
* 일부만 encoding
```python
from urllib import parse
>>> parse.quote('한글') #%ED%95%9C%EA%B8%80
>>> parse.unquote('%ED%95%9C%EA%B8%80') #한글
```
* 쿼리 string 전체 encode
```python
from urllib import parse
url = parse.urlparse('http://www.exeam.org?examParam1=value1&examParam2=한글') 
query = parse.parse_qs(url.query)
>>> parse.urlencode(query, doseq=True) #examParam2=%ED%95%9C%EA%B8%80&examParam1=value1
```
* tuple 이용시
```python
from urllib import parse
query = [('examParam1', 'value1'), ('examParam2', '한글')]
>>> parse.urlencode(query, encoding='UTF-8', doseq=True) #examParam1=value1&examParam2=%ED%95%9C%EA%B8%80
```
* dictionary 이용시
```python
from urllib import parse
query = {
         'examParam1' : 'value1',
         'examParam2' : '한글'
         }
>>> (parse.urlencode(query, encoding='UTF-8', doseq=True) #examParam1=value1&examParam2=%ED%95%9C%EA%B8%80
```

* 참고 : https://dololak.tistory.com/255


## 데이터 인코딩 깨질때 수정용 lib
* https://github.com/LuminosoInsight/python-ftfy
* 설치 pip install ftfy
``` python
a=ftfy.guess_bytes(in)
b=ftfy.fix_encoding(a[0])
c=ftfy.fix_text(b)
```

## save numpy to npy file
```python
import numpy as np
data = np.arange(100) # 저장하는 데이터
np.save('my_data.npy', data) # numpy.ndarray 저장. @파일명, @값
data2 = np.load('my_data.npy') # 데이터 로드. @파일명
```

