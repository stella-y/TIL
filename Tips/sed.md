* sed
	* 치환 - substitute (s/pattern/replace/)
		* 해당 패턴을 포함한 line remove
			```
			sed 's/pattern/d'
			```
		* 해당 패턴만 삭제
			```
			sed 's/\[//g'
			sed 's/\[//g' $embedding_path/before_sed.txt > $embedding_path/sed1.txt
			```
	* i option 주면 바꾼 상태로 파일 저장(tmp 파일 생성 후 동일 이름으로 다시 복사하는 방식)

