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

### upload existing project to git
```sh
git init
git add .
git commit -m "first commit"
git remote add origin <remote repository URL>
git remote -v
git push -u origin master
```

### remote repository
* 하나의 프로젝트를 여러 repository 에 저장할 수 있다(읽기 가능 레포, 읽기 쓰기 모두 가능한 레포 등으로 기능화해서 사용도 가능)
* remote repo 확인
```sh
git remote -v # remote repo 확인
# .git/config 에서도 확인 가능
git remote add <단축이름> <url> # 저장소 추가
git remote show <리모트 저장소 이름> #
git remote rename <a1> <a2> # a1의 alias 를 a2로 바꾼당
git remote remove <a2> # a2 repo 를 삭제
# 해당 리모트에 관련된 추적 브랜치 정보, 모든 설정내용 다 같이 삭제됨

git pull #remote repo branch 에서 데이터를 가져오기 + 자동으로 local branch 와 merge
git push <remote repo 이름> <branch> #해당 remote repo 의 해당 branch 로 push

```
* .git/config 에서도 확인 가능

### 이미 한 add, commit, push 취소하기
* git add 취소
	* 
참고 : https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html

