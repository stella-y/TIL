## cold start recommandation
* content / profile based methods
    * content: for new items
        * 음원 신호처리
        * (deep) collaborative topic regression
    * profile : for new users
        * DSSM
        * multi view DSSM
        * user linkage
* interview based methods
    * issue query(items) to a user
    * issue queries about a new item to users
    
* Definition of domain (domain levels)
	* attribute level(comedy <-> thriller)
		* same type of items, different values of certain attribute
	* type level (movies <-> books)
		* similar types, sharing some attributes
	* item level (movies <-> restaurants)
		* distinct types, differing in most, if not all attributes
	* system level (Netflix <-> movielens)
		* almost the same itmes, collected in different ways and/or from different operators
* cross-domain : opportunity or problem
	* source domain 이 bias가 되거나 noise 가 되거나
	 --> 근데 이건 weight 를 어떻게 주느냐에 대한 문제로 귀결됨
 	* two approaches
 			![approaches](images/crossdomain_1.png "approaches")
 		* linking/aggregating knowledge
 			* user preferences merge 하기
 			* user modeling data 를 중재함
 			* recommendations 를 combine 함
 			* domain 을 link 함
 		* sharing/transferring knwledge
 			* latent feature 를 share 함
 			* rating pattern 을 변환함

## proposed categorization
* linking/aggregating knowledge
	1. merging user preference
		* aggregate user preference
			* ratings, tags, transaction logs, click-through data
			* rating, tag, transaction log, click-through data 정보를 그대로 쓰는 것 (보통 시도하게 되는 그런것?) / 다른 도메인 정보들을 그냥 붙여버려
			![aggregate](images/crossdomain_2.png "aggregate")
			* pros
				* new-user problem 에는 좋아
				* robust
				* 설명이 용이함
			* cons
				* source 와 target domain 에 user-overlap 이 있어야돼
			* aggregate matrix 에는 single domain techniques 에 weight 를 주는 방식으로 해결할 수도 있어
				* ex
					* User-based kNN
						Berkovsky et al. 2007; Shapiraet al. 2013; Winoto& Tang 2008;
					* Graph-based
						Nakatsujiet al. 2010; Cremonesi et al. 2011; Tiroshiet al. 2013
					* Matrix Factorization / Factorization Machine
						Loniet al. 2014
	2. mediating user modeling data
		





			
