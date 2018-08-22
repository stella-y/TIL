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

### Information domain 학습
* objective function
	* regression based loss
* Attribute-aware Deep CF Model
	* Input layer / Embedding layer
	* Pooling layer
		* 유저 각각이 갖고 있는 attribute 의 수는 다를 것 → pooling layer 로 크게 맞추는게 편함
		* average pooling 이나 max pooling → inefficient! → user 와 attribute 사이의 pairwise correlation 을 modeling 하는 방식으로 pooling layer 제작 (item attribute 도 동일하게) / user 와 user attribute 간의 correlation + attribute 간 correlation 을 고려해서 pooling
	* Hidden layer
	* prediction layer

### Social domain 학습
* Graph regularization - (semi-supervised learning on graph)
* social user 와 아이템간의 score 를 구하려면 social user 의 information domain 에서의 latent vector 를 알아야 함 
	* → bridge user 들의 p_u(latent vector)를 전파 시키는 방법 
	* → 친밀도가 유사한 유저들은 item 에 대해서 유사한 preference 를 갖는다 (latent vector 가 유사할 것)
	* has two constraints : Smoothness & fitting
1. Smoothness : structural consistency
	* 가까운 유저는 유사한 representation 이 유사해야한다
	* smoothness constraint → social domain learning 유저의 latent vector 를 주변에 전파시키게 할 것
	* objective function
2. fitting : latent space consistency across two domains
	* bridge user 는 도메인간의 anchor 역할을 해줘야 함
	* 동일한 bridge user 는 동일한 representation 을 가져야 함
	* objective function
		* p_u' : information domain representation / p_u'(0) : social domain representation
* 두개의 latent space 를 연결해 주게 됨
* 두 constraints 합치장
* objective function
	* smoothness 와 fitting 에 대한 loss function 합침
	* 뮤 : 두 contstraints 의 tradeoff 를 컨트롤 할 positive parameter 
* Prediction for social user

### 전체 training 과정
1. observed item (u, i) 각각에 unobserved item (u, j)를 가져와서 triplet (u,i,j) 구성
2. gradient step 으로 loss function LI optimize → user 에 대해 enhance 된 representation 을 얻게 됨
3. enhance 된 representation 으로 social graph laplacian 에 반영 → social user 의 latent vector 를 update 함
4. drop out 추가 - pairwise pooling payer 에 dropout 추가 (p_u & q_i 구성할때 영향을 줄 수 있도록)

(수식, 그림 삽입 확인해야)