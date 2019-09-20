## Which anomaly detector should I use
- Anomaly detection
https://federation.edu.au/__data/assets/pdf_file/0011/443666/ICDM2018-Tutorial-Final.pdf

### 라이브러리
https://pyod.readthedocs.io/en/latest/

### outlier 구분
https://www.anblicks.com/resources/insights-blogs/an-introduction-to-outliers/
1. Global outlier
2. Contextual outlier
3. Collective outlier(전체적으로 봤을때에 issue)

### operational definitions of anomalies
1. distance-based or density-based def
- 이 점이 outlier 라면 주변에 다른 점들이 잘 없을것이다(density 가 낮을 것이다) 라는 가정
2. isolation-based method
- 이 점을 isolation 시키는데에 얼마나 많은 조건이 필요한가로 체크
3. zero++
- subsampling 을 했을때에 가장 잘 등장하지 않는 점은 outlier 일거란 가정

### 괜찮은 방법론
- Isolation Forest [1] (in general and in large feature space of unknown
quality) 
	- Liu, F. T., Ting, K. M., Zhou, Z .H. (2008) Isolation Forest. In Proceedings of IEEE ICDM, 413-422. 
- ABOD [2] and LOF [3] for highly clustered anomalies
	- [2] Kriegel, H-P., Schubert, M., Zimek, A. (2008) Angle-based outlier detection in high-dimensional data. In
Proceedings of KDD, 444-452.
	- [3] Breunig, M. M., Kriegel, H.-P., Ng, R. T., Sander, J. (2000) LOF: Identifying density-based local outliers. In: Proceedings of the ACM SIGMOD International Conference on Management of Data, 93-104 
- Isolation Forest [1] and LODA [4] scale well to **large data** sets while the other algorithms do not.
	- [4] Pevny, T. (2016) Loda: Lightweight On-line Detector of Anomalies. Machine Learning, 102(2), 275–304. 

### analytical result in a nutshell
1. the proportion of normal instances (or anomaly
contamination rate),
2. the nearest neighbour distances of anomalies in
the dataset,
3. sample size used by the anomaly detector where
the geometry of normal instances and anomalies
is best represented by the optimal sample size.
	- anamaly detection 은 다다익선이 아니더라아...
***page22***

* Characteristics of Ideal Anomaly Detectors
	• Few parameters
	• parameter-free the best
	• Easy to tune; not too sensitive to parameter setting
	• Fast runtime: can scale up to large datasets and high dimensional datasets
	• Low space complexity(knn 은 메모리를 엄청먹징)
	• Known behaviours under different data properties
	• Can deal with different types of anomalies:
	• Clustered anomalies vs scattered anomalies
	• Local anomalies vs global anomalies

* Isolation based methods
	* iForest, iNNE & aNNE
	* Start with iForest (ICDM2008), iNNE (workshop ICDM2014), aNNE (workshop ICDM2015)
	* iForest
		* 공간 분리하는 방식으로 각 점들을 tree 형태로 나타냄(isolation 시키기)
		* root 와 가까운 node 가 outlier 에 가깝다 라는 가정으로 isolation score 내놓음
		* **급한 약으로 괜찮음**
	* aNNE
		* x, y 로의 구분이 아니라 nn 방식으로 공간 분할

* KNN based methods
	* 느림
	* page 49?
	* 거리가 n 이상 / 거리가 k 이하인 점이 n 개 이하

* Angle-based anomaly detection
	* numerical 축이 아닌 categorical 에서는 angle 을 따로 정의할 필요가 생겨짐



* subspace anomaly detection


* feature bagging

* RS-hash(randomize hashing)







































