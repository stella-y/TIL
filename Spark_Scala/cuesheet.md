## cuesheet
* needs
	* 코드가 길어져서 ide의 도움이 필요해지거나, dependency 등등의 문제로 notebook 등의 활용보다는 scala project 를 작성하는게 낫다
	* --> 근데 이렇게 되면 submit 을 위한 shell script 를 따로 만드는 과정을 반복해야함
		* import spark as a 'provided' dependency
		* SBT-ASSEMBLY로 uber-jar 만들기
		* shell command에서 configuratin 설정 다 해줘야함	
https://www.ithome.com.tw/video/120391