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
* Metadata server가 없는 distributed parallel fault-tolerant file systems
* 대신 모든 서버들이 gluster storage pool에 어떤 서버들이 있고 이들을 사용한 어떤 볼륨들 있는지만 알고있을 뿐
	* —> glusterFS cluster내의 어떤 서버도 현재 mount 할 수 있는 볼륨의 정보를 얻을 수 있다
* 클라이언트, 서버로 구성
	* 서버 - brick이라는 형태로 제공 / 각 서버들은 glusterfsd 데본 을 실행해서 로컬 파일시스템을 볼륨으로 export
	* 클라이언트 - tcpip, infiniBand, sdp를 통해 서버로 연결을 하고 원격 서버들로부터 virtual volume을 구성함
* GlusterFS서버의 로컬 디스크에 지정된 폴더(brick)에 클라이언트가 보낸 파일을 변경 없이 그대로 저장
	*  E.g. 파일 10개를 3대의 glusterFS로 이뤄진 볼륨의 brick에 저장한다고 하면 세곳의 brick에 hash 알고리즘을 사용하여 분산저장한다
* 모든 파일의 정보는 GlusterFS 클라이언트가 volumn을 mount하면 그때 볼륨에 속한 GlusterFS 서버의 brick으로 지정된 폴더에서 일어와 한 폴더이야 일종의 가상으로 파일들을 보여준다
	* —> metadata서버에 파일 정보를 물어볼 필요 없이 자신이 마운트한 glusterfs 의 볼륨 정보만 알면 된다.
* 클라이언트 방식
	* NFS, CIFS, Gluster Native(FUSE) 방식 제공
	* Nfs로 마운트
		* Mount -t nfs [볼륨위치] [마운트 위치]
	* Gluster Native(FUSE)로 마운트
		* Mount -t gluster [볼륨위치] [마운트 위치]
