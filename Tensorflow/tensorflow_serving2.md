## Tensorflow serving 2
### 두개 이상의 모델 한번에 서빙하기(모델 버전관리)
1. 서빙하고자하는 모델의 checkpoint 를 serialize 시켜둔다.
```
└── serve
    ├── comment07_model
    │   ├── 1
    │   │   ├── saved_model.pb
    │   │   └── variables
    │   │       ├── variables.data-00000-of-00001
    │   │       └── variables.index
    │   ├── 2
    │   │   ├── saved_model.pb
    │   │   └── variables
    │   │       ├── variables.data-00000-of-00001
    │   │       └── variables.index
    │   ├── 3
    │   │   ├── saved_model.pb
    │   │   └── variables
    │   │       ├── variables.data-00000-of-00001
    │   │       └── variables.index
    │   ├── 4
    │   │   ├── saved_model.pb
    │   │   └── variables
    │   │       ├── variables.data-00000-of-00001
    │   │       └── variables.index
    │   └── 5
    │       ├── saved_model.pb
    │       └── variables
    │           ├── variables.data-00000-of-00001
    │           └── variables.index

```

2. 돌아가고 있던 serving docker 를 종료하고, container 를 삭제
```sh
docker stop [contanier_id]
docker rm [contanier_id]
```

3. docker 에 넣을 config file 을 생성(models.config)
	* 가동시킬 모델 리스트를 아래와 같이 정의해서, 실행시킬 모델의 위치를 정확하게 지정할 수 있음
```sh
model_config_list {
  config {
    name: 'my_first_model'
    base_path: '/tmp/my_first_model/'
  }
  config {
    name: 'my_second_model'
    base_path: '/tmp/my_second_model/'
  }
}
```
	* 또는 model_version_policy를 정의해서, 동일 모델에서 어떤 버전을 실행시킬지 지정할 수 있음(이 부분이 tensorflow serving 공식가이드에서 model_version_policy 부분만 적혀있어서 매우 헷갈렸음)
```sh
model_config_list: {
  config: {
    name: "comment07_model"
    base_path: "/models/comment07_model"
    model_platform: "tensorflow"
    model_version_policy: {
    	model_version_policy {
  			specific {
    			versions: 42
    			versions: 43
  			}
		}
    }
  }
}

```
	* 해당 모델의 모든 버전들을 서빙가능하게 만들 수도 있다(자꾸 config 수정하기 싫으면 이게 좋음-내가 쓰는 방법...)
```sh
model_config_list: {
  config: {
    name: "comment07_model"
    base_path: "/models/comment07_model"
    model_platform: "tensorflow"
    model_version_policy: {
      all: {
      }
    }
  }
}
```

4. docker 컨테이너 만들어서, 그 안에 모델과 config file 넣기
```sh
docker run -d --name comment_model_test tensorflow/serving:latest-gpu
docker cp /data1/ml_gpu_jupyter_sshd/stella-y/comment_model/serve/comment07_model comment_model_test:/models/comment07_model
docker cp /data1/ml_gpu_jupyter_sshd/stella-y/comment_model/config comment_model_test:/config
docker commit --change "ENV MODEL_NAME comment07_model" comment_model_test comment_model
```

5. gpu로 container 실행(with config 조건)
```sh
NV_GPU=7 nvidia-docker run -p 8501:8501 comment_model --model_config_file="/config/models.config"
```


