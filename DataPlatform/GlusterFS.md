## Gluster fs 
* 기존의 distributed parallel faulttolerant file systems --> e.g. hdfs
* File system 으로서의 Hdfs(Hadoop distributed file system)
  * Data node - 하나의 스토리지를 포함한 서버
  * Name node - metadata 서버에 읽으려는 파일의 분산된 위치를 받아서 직접 분산되어 저장된 datanode 서버에서 파일 조각들과 직접 접근한다
    * —> 메타데이터 서버를 통해 데이터 노드 서버에 흩어져 있는 파일 정보를 한곳에서 확인할 수 있고, 파일을 여러 클라이언트에서 접근하게 되면 locking문제들도 해결된다
		* + datanode 서버 풀 관리, 볼륨 관리, 로그 관리 등등 (중앙 집중적 관리를 위해 필요)
		* + namenode 서버의 어디에 저장할지 요청하여 알려주는 곳에 파일을 block단위(hdfs 에서는 64mega)로 쪼개서 저장함
		* + block들의 복제본을 만들어서 datanode가 다운되어, 다른 datanode에 있는 복사본 block이 원본의 역할을 대신함
		* —> datanode 서버만 증가하면 용량과 총 처리 능력이 선형적으로 증가할 수 있음
  * 근데 여기서는 문제점 —> metadata 서버가 죽으면 어떻게 할 것이냐…
		* 보통은 이중화로 해결
	* 그래도 문제점 —> cloud환경에서는 동적으로 증가하는 스토리지 볼륨 필요
		* 파일들이 계속해서 증가해간다면 metadata서버는 견딜 수 있을 것인가 / 이중화 하더라도 metadata서버에 의한 병목 현상을 발생하지 않을 것인가
—>gluster file system(Gluster FS)
	• Metadata server가 없는 distributed parallel fault-tolerant file systems
	--ㄱㅖㅅㅗㄱ...
	

