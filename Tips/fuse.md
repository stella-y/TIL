## Filesystem in USErspace(FUSE)
* HDFS 는 VFS 인터페이스에 맞춰서 구현되지 않아 일반 파일처럼 읽고 쓰는게 매우 힘듦
* 이 형식에 맞춘것처럼 접근할 수 있게 해주는게 fuse
* fuse 로 hdfs mount
	1. setproxy wget http://archive.cloudera.com/cdh5/one-click-install/trusty/amd64/cdh5-repository_1.0_all.deb
	2. sudo dpkg -i cdh5-repository_1.0_all.deb
	3. (sudo -i apt-key update)
	sudo -i setproxy apt-get update
	4. sudo -i setproxy apt-get install hadoop-hdfs-fuse
	5. sudo mkdir -p /mnt/aa-hadoop : mount point 지정
	6. /etc/fstab 수정
	```
	hadoop-fuse-dfs#dfs://aa-hadoop-nn2.dakao.io:8020        /mnt/aa-hadoop          fuse    usetrash,big_writes,rw,nonempty 2 0
	```
	7. sudo mount /mnt/aa
	8. 끗

### fuse restart
* 퓨즈를 안심하고 막쓰다보면 곧 맛이 간다... --> 되도록 하둡명령어를 쓰자...
* fuse 메모리 사용량이 너무 증가할때에... --> kill 시켜버리고 unmount 하자
* unmount & mount
	```sh
	# unmount
	sudo fusermount -u /mnt/aa-hadoop
	sudo mount /mnt/aa-hadoop
	```
