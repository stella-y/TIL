## Density clustering
### DBScan
![DBScan](image/3_1.png "DBScan")
* 밀도 기반 clustering
	* 어느 점을 기준으로 반경 x 내에 점이 n 개 이상 있으면 하나의 군집으로 인식하는 방식
* parameter : e(epsilon), m(mininum points)
	(p(기준점))
	* 거리 e 내에 점이 m 개 있으면 하나의 군집으로 인식
	* 이 조건을 만족하는 점(e 내에 점 m 개를 가지고 있는 점) p를 core point(중심점) 이라고 한다
* 방식
	* 각 점에 대해 e 내에 점이 m 개 있는지를 확인
	* 있다면 이 점을 core point 로 한 cluster 로 인식(core point 가 아닌 나머지 점들은 border point)
	* 점의 border point 중 다른 cluster 에 core point 가 포함돼있다면, 이두기의 cluster 는 하나의 cluster로 merge
	* 어떤 점을 중심으로 해도 거리 e 내에 점 m 개가 존재하지 않는 점은 noise point (outlier 로 취급함)

* 장점
	* cluster 의 갯수를 사전에 정하지 않아도 됨
	* 군집 밀도에 따라 클러스터를 서로 연결하기때문에 cluster 모양이 특이해도 잘 찾는다
	* noise point 이용해서 outlier 를 잘 찾아낸다
* 단점
	* 두개 이상의 cluster 에 속한 border points 들이 생길 수 있다
	* cluster 들이 다양한 밀도를 갖고 있다면 cluster 찾아내기 어려울 수도 있다


--> 이거 보완하려고 나온 알고리즘이 hdbscan
Dbscan 에서 noise로 분류된 지점들을 outlier 나 abnormaly 로 가져옴

참고 : https://bcho.tistory.com/1205