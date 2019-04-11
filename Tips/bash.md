## sed
* (=stream editor)
* 텍스트 변환 유틸
* 줄단위(\n)처리를 함
* 줄단위 처리가 기본이지만 메모리를 이용해 여러줄 처리도 가능

### 줄 치환
```sh
sed -i "s/변경전문자열/변경후문자열/g" [파일]
```
### 줄 삭제
```sh
$ echo -e "aaa\nbbb\nccc\nddd" | sed "2d"
aaa
ccc
ddd
```
### 특정파일 특정 줄에만 접근
```bash
sed -n 56063p entertain_3mon_like_title.csv
```
56063번째줄만 읽기



## awk

https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_sed
https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_awk
