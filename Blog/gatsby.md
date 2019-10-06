# static site, JAM stack site, SPA
## 정적 사이트
* html, css, javascript, 이미지등의 정적 파일만 cdn 등을 통해서 배포
	* --> 별도의 서버 운영이 필요 없음
	* --> 사용자가 많아져도 서버 부하가 생길걸 걱정할 필요도 없음

## JAMstack site
* client-side javascript + reusable APIs + prebuilt Markdown
* 템플릿은 미리 만들어서 javascript 와 함께 배포하고, api 로 데이터 불러오는 사이트

### 포함관계
* API 를 전혀 안쓰는 정적 사이트는 jam
* jam stack 이 정적사이트는 아니다(api 를 쓰기 때문)

## SPA(Single Page Application)
* html + javascript 
* 이후 javascript 가 실행되면서 api 로 데이터 불러오고, markup 으로 화면 보내주고, 사용자 이동에 맞춰서 push state 로 history 를 바꿔주면서 page 를 보여주지만 실제로는 모두 프론트엔드에서 처리된다

## Gatsby
* react 사용법을 크게 해치지 않으면서 웹사이트를 만들수 있도록 잘 감사서 제공
* 작동방식
	* 데이터 소스(gatsby 에서 데이터 가져오는 곳을 이렇게 부름)
		* wordpress 같은 cms 도구 / 다른 정적 사이트 생성기처럼 markdown 파일 / api 등으로 가져오는 형태
* GraphQL
	* gatsby 는 기본적으로 graphql 을 사용해서 데이터 가져오게 됨
	* (플러그인 이용해서 가져올 수도 있지만 graphql 이 gatsby 에 포함되어 있어서 훨씬 쉽게 슬 수 있는 것)
* gatsby 는 react 를 이용해서 만든다
* 공통 레이아웃 관리, 페이지생성, 데이터 소스와 컴포넌트 연결 등등을 다 gatsby 에서 제공함 / 빌드하면 정적 사이트로 만들어 준다.
	* 데이터 소스에서 graphQL로 가져온 데이터를 빌드할 대 모두 가져와서 정적 파일의 데이터로 포함시켜버림
	* **빌드 시에 graphQL로 데이터 가져와서 빌드된 배포 파일에 포함시킨다 /-> 정적 사이트로 만들어주는 것**

## 기본 동작과정
* '''npx gatsby-cli new gatsby-example''' : 기본 웹사이트 생성
* '''npm run develop (= gatsby develop) ''' : 개발모드로 서버 실행 (http://localhost:8000/)
	* 개발모드에서는 graphQL 을 테스트하기 쉽게 GraphiQL 이 포함되어있다.
* '''npm run build (= gatsby build)''' : 프로덕션용 정적 사이트 빌드
	* 이 때 빌드 결과로 개발버전대모다도 더 많은 파일이 막 생기는데 이건 최적화를 위한 것

참고:
https://blog.outsider.ne.kr/1426
https://blog.outsider.ne.kr/1417











