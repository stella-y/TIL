## NSCR(Neural Social Collaborative Ranking)
* Item Silk Road: Recommending Items from Information Domains to Social Users (SigIR 2017)

### main idea
Information domain 정보에 graph regularization 으로 친구 관계를 결합시켜 학습
* Information domain
	* user와 item 간 interaction + user의 attribute + item 의 attribute 으로 구성
* Social Domain
	* 서비스 사용경험이 있는 user와의 친밀한 정도로 신규 유저의 preference 예측

### Input / Output
* Input
	* Information domain : {U1, I, Y, Gu , Gi }
		* U1 : user set / I : item set / Y : user 와 item 간 interactions, Y = {yui} / Gu : user attribute(속성) / Gi: item attribute(속성)
	* social domain : {U2, S} 
		* U2 : social domain 에서의 user set / S : 모든 social connection, S={su′u′′}
	* 단, U1 ∩ U2 is nonempty
* Output
	* fu': I→R (fu' : personalized ranking function)
	* R : social domain 의 유저 u' 각각을 I 에 존재하는 모든 item 에 real number 로 매핑(랭킹 점수)
