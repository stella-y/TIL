## RNN 이용한 nlp
* nlp --> word, character, sentence 관점에서 sequence data 로 볼 수 있음
![rnn](images/5_1.png "rnn")
![rnn2](images/5_2.png "rnn2")
* rnn training - unrolled graph is a well-formed (DAG) computation graph
* rnn 으로 하면 --
	* 문장 전체를 읽고 prediction 하는게 가능해짐
	* 문장 내 context표현 가능
	* 활용 - tagging / language model(각 태그가 next word 인 tagging job 으로 볼 수 있음) / calculating representations for parsing
