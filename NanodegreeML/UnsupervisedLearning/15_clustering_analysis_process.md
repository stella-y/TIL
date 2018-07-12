* Clustering validation(compactness / separability)
	* category
		* External indices
			* Labeled data
		* Internal indices
			* 답이 없을 때(unsupervised learning)
		* Relative indices
			* 어떤 clustering structure 가 더 나은가
	* Compactness
		* Cluster 의 element 들이 얼마나 가까운가
	* Separability
		* 서로 다른 cluster 들이 얼마나 멀리 있는가
* External validation indices
	* adjusted rand score 등...
	![validation_indices](image/15_1.png "validation_indices")
	* labeled dataset 의 경우의 scoring methods
	* Adjusted rand index
	![Adjusted_rand_index](image/15_2.png "Adjusted_rand_index")
		* A - 같은데 있는 두개가 같은데 있는 경우
		* B - 다른데 있는 두개가 다른데 있는 경우
