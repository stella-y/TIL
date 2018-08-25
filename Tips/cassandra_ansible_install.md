1. Ansible 설치
	a. Control machine 은 gcc compiler 와 python 개발 패키지가 설치 돼 있어야 함yum install python-devel
	b. Epel repository 설치 
		i. rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
		ii. Yum repolist -> 에러 없이 정상 처리 돼야
			1) 에러 생기면 
				a) /etc/yum.repos.d/epel.repo 에서 epel, epel-debuginfo, epel-source 의 base url 의 주석 해제, mirrorlist 주석 & enable=1
	c. Ansible 설치
		yum install ansible -y
	d. /etc/ansible/hosts 파일에서 설치할 호스트 지정
	e. Setup ssh
		ssh-keygen –t rsa
ssh-copy-id root@MYHOSTNAME1
ssh-copy-id root@MYHOSTNAME2
	f. 설치 확인
		i. Ansible ping 모듈 실행
		ansible all -m ping  -k
