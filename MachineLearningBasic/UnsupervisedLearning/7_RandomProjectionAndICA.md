## Random Projection
* One of the dimension reduction method
	* PCA 보다 computationally 더 효율적이다
	* 아무 축이나 만들어서 projection 시켜버려
	![rp](image/8_1.png "rp")
	* Random matrix 에 multiply 해서 dimension 만 맞춰
	* Johnson-Lindenstrauss lemma 에 의해서 n개의 포인트가 있을 때에 차원 축소 이후에도 그 포인트 간의 거리는 유지될 수도 있다
	![rp](image/8_2.png "rp")
	* 이 지점을 어떻게 찾는가!
		* Eps 는 차원 축소 후 발생하는 error 를 얼마나 허용할 것인가를 뜻함
		* 아래와 같은 조건으로
		![rp](image/8_3.png "rp")

## ICA
* Independent Component Analysis
	* Pca - maximize variance / 
	* Ica - feature 들은 독립적인 source 들의 mixture 로 봐
	* 이 독립적인 source 들을 dataset 에서 추출해 낸다는 개념
	* 대표적인 예 - 칵테일 파티 문제 / blind source separation
	![ica_concept](image/8_4.png "ica_concept")
* fastICA algorithm
	1. center, whiten x
	2. choose initial random weight matrix w1, w2, w3,...
	3. estimate w, containing vectors
	4. decorrelate w
	5. repeat from step #3 until converged
	![factica](image/8_5.png "factica")
