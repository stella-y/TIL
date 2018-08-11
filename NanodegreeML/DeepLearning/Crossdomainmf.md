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



			
