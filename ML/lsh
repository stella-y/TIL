## LSH(Locality sensitive hash)

* why : 그냥 hashtable 을 이용하면 와전히 유사한 값도 유사한 hashcode 를 갖게 될 수있다
* --> 완벽히 동일한 값에 대해서는 detect 가 가능해지지만, nearly duplicated 한 값들에 대해서는 전혀 detect 되지 못할 것
* 이의 해결을 위해 서로 다른 hash table 로 동일한 과정을 반복하게 됨
* --> 서로 다른 hash table 을 이용하여 hashcode 의 생성을 반복하다보면, 충분히 유사한 값들에 대해서는 언젠가는 동일한 hash Code 를 밷어내게 될 것이다 를 가정으로 세운 것!
