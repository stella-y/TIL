# 간단 gatsby 정리
## static site, JAM stack site, SPA
gatsby 정리 전 static site, JAM stack site, SPA가 뭔지와 그 포함관계를 먼저 보자.
* 정적 사이트
	* html, css, javascript, 이미지등의 정적 파일만 cdn 등을 통해서 배포
		* --> 별도의 서버 운영이 필요 없음
		* --> 사용자가 많아져도 서버 부하가 생길걸 걱정할 필요도 없음

* JAMstack site
	* client-side javascript + reusable APIs + prebuilt Markdown
	* 템플릿은 미리 만들어서 javascript 와 함께 배포하고, api 로 데이터 불러오는 사이트

* 포함관계
	* API 를 전혀 안쓰는 정적 사이트는 jam
	* jam stack 이 정적사이트는 아니다(api 를 쓰기 때문)

* SPA(Single Page Application)
	* html + javascript 
	* 이후 javascript 가 실행되면서 api 로 데이터 불러오고, markup 으로 화면 보내주고, 사용자 이동에 맞춰서 push state 로 history 를 바꿔주면서 page 를 보여주지만 실제로는 모두 프론트엔드에서 처리된다

## Gatsby
* react 사용법을 크게 해치지 않으면서 웹사이트를 만들수 있도록 잘 감싸서 제공한다
* 작동방식
	* 데이터 소스(gatsby 에서 데이터 가져오는 곳을 이렇게 부름)
		* wordpress 같은 cms 도구 / 다른 정적 사이트 생성기처럼 markdown 파일 / api 등으로 가져오는 형태 등이 있을 것 
	* 데이터 소스 가져오느는 방법 - GraphQL
		* gatsby 는 기본적으로 graphql 을 사용해서 데이터 가져오게 됨
		* (플러그인 이용해서 가져올 수도 있지만 graphql 이 gatsby 에 포함되어 있어서 훨씬 쉽게 쓸 수 있다!)
	* 웹사이트 구성
		* gatsby 는 react 를 이용해서 만든다
		* 공통 레이아웃 관리, 페이지생성, 데이터 소스와 컴포넌트 연결 등등을 다 gatsby 에서 제공함 / 빌드하면 **정적 사이트**로 만들어 준다.
			* 데이터 소스에서 graphQL로 가져온 데이터를 빌드할 대 모두 가져와서 정적 파일의 데이터로 포함시켜버리기 때문에 SPA(api 통해서 데이터 소스를 가져온다)가 아닌 정적 사이트라고 말하는게 더 맞다
	* static web host 를 이용한 deploy
		* 위에서 구성한 페이지(html, css, react로 구성될 것)는 AWS Amplify, netlify, github pages 등의 statkc web host 를 통해서 deploy 될 수 있다!
		* 이 전체 과정은 아래 그림을 참고하면 더 쉽게 이해할 수 있다!
		![gatsby](image1.png "gatsby 동작방식 - from https://www.gatsbyjs.org/")


### graphQL 간단 정리
* 어플리케이션에서 데이터를 가져올때 통상적으로 쓰는 방법이 restAPI 를 구현하는 것일것이다 --> 하지만 어플리케이션 규모가 커지면 너무 많은 api endpoint 가 생겨날 수 밖에 없게 될것...
* 그래서 api call 대신 '필요한 정보를 쿼리 형태로 서버에 전달하고, 서버가 이 쿼리에 맞게 데이터를 보내주게 하자'의 idea 에서 탄생한게 graph ql 이다!
* 쿼리를 통하여 딱 필요한 데이터만 fetching 을 하기 때문에 overfetch 혹은 underfetch 를 할 걱정을 할 필요가 없다!

### netlify
* 정적 사이트의 호스팅, 자동빌드/배포, dns, ssl, cdn  설정 등의 사이트 관리 기능을 무료로 제공함
* node, rubym python 빌드를 제공해서, 직접 빌드하고 업로드 할 필요가 없다
* deploy 하고자하는 gatsby blog를 깃 레포에 올리고 이 레포 명을 netlify 에 등록해 놓으면, 알아서 빌드 후 디플로이 해준다!

## 기본 조작 방법
* '''npx gatsby-cli new gatsby-example''' : 기본 웹사이트 생성
* '''npm run develop (= gatsby develop) ''' : 개발모드로 서버 실행 (http://localhost:8000/)
	* 개발모드에서는 graphQL 을 테스트하기 쉽게 GraphiQL 이 포함되어있다.
* '''npm run build (= gatsby build)''' : 프로덕션용 정적 사이트 빌드
	* 이 때 빌드 결과로 개발버전대모다도 더 많은 파일이 막 생기는데 이건 최적화를 위한 것
* (물론 이 과정을 하기 전에 node.js, gatsby client 등을 다 설치해둬야한다... ㅎㅎ)

참고:
https://blog.outsider.ne.kr/1426
https://blog.outsider.ne.kr/1417
https://velopert.com/2318










