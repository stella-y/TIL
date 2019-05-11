## LSH(Locality sensitive hash)
* why : 그냥 hashtable 을 이용하면 유사한 값도 유사한 hashcode 를 갖지 못할 수 있다
* --> 완벽히 동일한 값에 대해서는 detect 가 가능해지지만, nearly duplicated 한 값들에 대해서는 전혀 detect 되지 못할 것
* 이의 해결을 위해 서로 다른 hash table 로 동일한 과정을 반복하게 됨
* --> 서로 다른 hash table 을 이용하여 hashcode 의 생성을 반복하다보면, 충분히 유사한 값들에 대해서는 언젠가는 동일한 hash Code 를 밷어내게 될 것이다 를 가정으로 세운 것!
* how
	1. (vector space 내에서 얘들을 normalize 시켜서 둠)
	2. random 한 hyper plane 몇개 생성
	3. code 화 해야할 점들을 hyper plane 을 기준으로 encode(점이 plane 내부면 1, 외부면 0 이런 식으로)
	4. hyper plane 을 또 생성해서 위의 과정 반복
유사한 vector 는 동일한 hashcode 값을 갖게 되는 부분이 생기게 될 것
* computational cost

https://www.youtube.com/watch?v=Arni-zkqMBA