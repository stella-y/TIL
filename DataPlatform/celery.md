# celery
* 웹서비스에서 응답 받기 오래걸리는 작업이 있는 경우 --> 비동기로 작업은 처리하게 하고, 응답은 즉각적으로 보내게 하는게 좋음
* 이 때 비동기로 돌아가야할 Task를 Brocker(message queue)에 쌓아두고, 각각 독립된 Worker 프로세스들은 새로운 일거리(Task)가 없는지 지속적으로 Task queue 를 감시하게 하는게 celery 의 컨셉
* 메시지(message)를 통해 통신, Broker(rabbitMQ 같은) 클라이언트와 워커 사이에서 메시지를 중계
브로커는 클라이언트가 큐에 새로 추가한 태스크를 메시지로 워커에 전달
* 셀러리 시스템에서는 여러개의 워커와 브로커를 함께 사용 가능 --> 높은 가용성과 Scaling이 가능

## rabbitMQ
### rabbitMQ 설치, 실행
```sh
#설치
wget -O - "https://packagecloud.io/rabbitmq/rabbitmq-server/gpgkey" | sudo apt-key add -
sudo apt-get install apt-transport-https

#실행
sudo rabbitmqctl add_user admin admin # 유저 추가 (user : admin / password : admin)
sudo rabbitmqctl add_vhost target_vhost # target_vhost 로 virtual host setting
sudo rabbitmqctl set_user_tags admin admin # user name 에 tag 달기 (user admin 의 tag 는 admin 인 것)
sudo rabbitmqctl set_permissions -p target_vhost admin ".*" ".*" ".*" # user admin 에게 target_vhost 에 대한 permition 을 부여함

sudo rabbitmq-server # 실행
sudo rabbitmq-server -detached # background 실행
sudo rabbitmqctl stop 중단
```

### rabbitMQ admin page
- rabbitmq-server 실행시켜둔 다음에, plugin 을 실행
```sh
sudo rabbitmq-plugins enable rabbitmq_management
```
- rabbit mq 관리 페이지에 접속이 가능하다
- 페이지 접속에는 위에서 설정한 user name과 password 를 사용한다
- 15672 포트로 접속이 가능하다

## celery
### celery 설치
```sh
pip install celery
```
### celery script 작성
* return 이 꼭 필요하지 않다면 ignore_result 를 true 로 설정해서 속도를 향상시키자.
```python
#celery_test.py
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task(ignore_result=True)
def add(x, y):
    return x + y
```

### celery server 띄우기
```sh
#celery -A [celery script 이름] worker --loglevel=info
celery -A celery_app worker --loglevel=info
```

### task 던질 script 작성
```python
#test.py
import random
from celery_test import add
result=add.delay(random.randint(0,100), random.randint(0,100))

result.get()
```

### flower
* celery 의 모니터링 툴
* query 나 task 의 상태 확인이 가능하다

```sh
#설치
pip install flower

#실행
#celery flower -A proj --address=127.0.0.1 --port=5555
celery flower -A celery_app worker --loglevel=info --port=5555
```




### 참고
http://docs.celeryproject.org/en/latest/getting-started/index.html
http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker
https://medium.com/sunhyoups-story/celery-b96eb337b9cf#.k1ka79f3w
ignore_result 관련 - https://www.slideshare.net/kkungkkung/celery-52212762
multi worker 등 관련 - https://docs.celeryproject.org/en/latest/userguide/workers.html
https://calyfactory.github.io/celery%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-worker%EC%B2%98%EB%A6%AC%EB%A5%BC-%ED%95%B4%EB%B3%B4%EC%9E%90
celery flower 관련 - https://wikidocs.net/11887
