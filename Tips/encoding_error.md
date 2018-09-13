## 데이터 인코딩 깨질때 수정용 lib
* https://github.com/LuminosoInsight/python-ftfy
* 설치 pip install ftfy
``` python
a=ftfy.guess_bytes(in)
b=ftfy.fix_encoding(a[0])
c=ftfy.fix_text(b)
```
