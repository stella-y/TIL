## kerberos 프로토콜
* 분산 환경에서의 네트워크 인증 프로토콜
* 1. 클라이언트/서버 외 제 3의 인증 서버(authentication server) 도입, 2. 이와 연동된 티켓 부여 서버(Ticket Granting Service, TGS) 통해서 티켓 발급 3. 유효한 티켓이 있는 유저만 서비스 서버(Service server) 에 접속할 수 있도록 제어
![kerberos](image/kerberos_1.PNG "kerberos")
1. client : 인증 서버에게 패스워드 전송하여 인증 요청
2. authentication server : User Id 가 db 에 존재하는지 찾아본 후 TGS 에 대한 티켓을 포함하여 응답 보냄
	1. client PWD 기반 비밀키 로 TGS session key를 암호화
	2. 티켓을 발급 받을 수 있는 티켓(TGT:Ticket-Granting-Ticket) - TGS 비밀키로 'Client ID, 주소, 유효기간, TGS 세션 키'를 암호화
3. client : TGS 에 ticket 요청(아래 두 메시지로)
	1. authenticator(TGS 세션키로 clientID, timestamp를 암호화)
	2. TGT (클라이언트는 TGS 비밀키를 몰라서 복호화, 데이터 조작이 불가함)
4. TGS : TGT와 Authenticator 를 복호화해서 client key 일치하는지 확인후, 티켓이 포함된 응답 리턴함(아래 두개 메시지)
	1. TGS 세션키로 암호화한 Service server 세션키
	2. Ticket - SS 비밀키로 client Id, 주소, 유효기간, SS session 암호화한 값
5. client 가 아래 메시지(credential)로 service server 에 서비스를 요청
	1. authenticator (SS 세션키로 client id, timestamp 암호화한 값)
	2. ticket
6. service 가 응답하고 access 권한 부여됨
	- service server 가 전달받은 ticket, authenticator 를 복호화한 후, client id 일치 여부 확인 후, 권한 부여

### terminology
* KDC(Key Distribution Center) : AS(Authentication server) + TGS(Ticket-Granting Service)를 제공하는 네트워크 서비스
* realm(영역) : 한 kerberos 시스템에 속해있는 client\~server 의 범위
* ticket : kerberos 프로토콜 인증 수단 / 아래 내용 포함함
	1. 서버, 클라이언트 ID
	2. 클라이언트 네트워크 주소
	3. 티켓 유효기간
	4. clieht-server 간 공유되는 session 키
* credential
	* TGT 가 client 에 발급
	* ticket+authenticator 로 구성
* authenticator : client id, timestam 를 ss session key 로 암호화한 값

### hadoop kerveros
1. 모든 하둡서비스는 KDC 에 자신을 인증하고, 데이터 노드에 네임노드 등록 / 태스크 트래커도 잡 트래커에 등록하고, 노드매니저는 리소스매니저에 등록
2. client 가 kdc 에 인증
	- client 는 namenode 와 job tracker/ resource manager 에 대한 service ticket 요청
3. hdfs 내 파일 접근 위해 client 는 namenode 에 접속하고 파일 요청
	- namenode 는 client 인증 후, block access tocken 으로 client 에 인증정보 제공
	- datanode 는 사용자에게 block access tocken 을 요청해서 client 권한 확인 후, 요청 block 에 대한 접근을 제공함
4. hadoop cluster 에 map reduce job 을 제출하기 전, job tracker 는 client 에 위임토큰 요청
	- 이 위임토큰은 cluster 에 MR 잡을 제출할때 이용 됨
	- job tracker 는 긴 시간 수행되는 잡을 위해 이 위임 토큰을 갱신한다


* 참고:
https://www.letmecompile.com/kerberos-protocol/
https://docops.ca.com/ca-single-sign-on/12-7/kr/kerberos-401457696.html
https://woounnan.tistory.com/38
https://as9070.tistory.com/109?category=683175