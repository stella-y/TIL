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

## pandas dataframe merge
* pandas dataframe 을 merge 할때에 메모리에러가 나는 경우가 있다.
* merge 할 대상 dataframe 두개와 새로 만드는 dataframe 을 다 메모리에 올려둬야 해서 이런일이 생기게 되는것
* 이때 pandas.read_csv에서의 chunk option 을 이용하게 하면 쉬워진다.
```python
df1 = pd.read_csv("yourdata.csv")
df2 = pd.read_csv("yourdata2.csv")
df2_key = df2.Colname2

# creating a empty bucket to save result
df_result = pd.DataFrame(columns=(df1.columns.append(df2.columns)).unique())
df_result.to_csv("df3.csv",index_label=False)

# save data which only appear in df1 # sorry I was doing left join here. no need to run below two line.
# df_result = df1[df1.Colname1.isin(df2.Colname2)!=True]
# df_result.to_csv("df3.csv",index_label=False, mode="a")

# deleting df2 to save memory
del(df2)

def preprocess(x):
    df2=pd.merge(df1,x, left_on = "Colname1", right_on = "Colname2")
    df2.to_csv("df3.csv",mode="a",header=False,index=False)

reader = pd.read_csv("yourdata2.csv", chunksize=1000) # chunksize depends with you colsize

[preprocess(r) for r in reader]
```
- 참고 : https://stackoverflow.com/questions/47386405/memoryerror-when-i-merge-two-pandas-data-frames

## heapq
* heapqpushpop 과 heapreplace 의 차이
	* heapq.heappushpop(pool, val) : pop 전에 val push 먼저 진행
	* heapq.heapreplace(pool, val) : 현재 삽입하는 val에 관계 없이 pool 에서 가장 작았던 값 반환
* heapq.nlargest(n, iterable[, key])
	* Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]

## itertool
https://hamait.tistory.com/803

## __future__ 모듈
* python3.x 에서의 기능을 python2.x 에서 쓸 수 있게 해주는 모듈
```python
from __future__ import print_function
print ("hello", "world")
# hello world
```