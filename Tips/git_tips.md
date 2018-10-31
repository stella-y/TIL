### git 에 너무 큰 파일 잘못 push 해서 에러날때;;
* 기존 Commit에서 100MB보다 큰 파일의 로그를 강제로 없애줘야 한다
* https://rtyley.github.io/bfg-repo-cleaner/ 다운로드 후
``` bash
java -jar bfg-x.x.x.jar --strip-blobs-bigger-than 100M
-- 위에서 에러나면
git repack && git gc
-- 이거 먼저 하고 다시
```
참고 - https://medium.com/@stargt/github%EC%97%90-100mb-%EC%9D%B4%EC%83%81%EC%9D%98-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EC%98%AC%EB%A6%AC%EB%8A%94-%EB%B0%A9%EB%B2%95-9d9e6e3b94ef