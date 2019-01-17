## cuesheet
* needs
	* 코드가 길어져서 ide의 도움이 필요해지거나, dependency 등등의 문제로 notebook 등의 활용보다는 scala project 를 작성하는게 낫다
	* --> 근데 이렇게 되면 submit 을 위한 shell script 를 따로 만드는 과정을 반복해야함
		* import spark as a 'provided' dependency
		* SBT-ASSEMBLY로 uber-jar 만들기
		* shell command에서 configuration 설정 다 해줘야함	
* cuesheet
	* abstract base class
	* spark-shell 에 있는 것 처럼 만들어주는 프로그램
	* jvm main class 로 동작하게 됨
	--> ide로부터 곧바로 spark application 을 실행시키게 함
* Configuration management
	* sc 등 넣을걸로, configuration file 따로 만들어서 application.conf 에 classpath resource 로 넣어둬
	* 일반적인 spark configuration
	* yarn configuration & options
		* yarn cluster 관련 - size, memory, # of instances 등등
		* hadoop configuration download 하고 create 할 xml file
	* configuration, business logic, deployment 가 각각 분리됨
* Ide 안에서 submit 하고 debugging을 다 해버리는게 가능해짐
https://www.ithome.com.tw/video/120391

* cuesheet 을 이용하지 않고, ide와 scala spark 을 같이 쓰는 법
	* http://cyberx.tistory.com/143
	* http://www.devinline.com/2016/01/apache-spark-setup-in-eclipse-scala-ide.html
	* https://www.slideshare.net/DOHYUNGPARK2/ss-75269927
	* http://scala-ide.org/
--> jar 로 뽑아낸 후 shell 에서 spark-submit 실행시키는 방식
