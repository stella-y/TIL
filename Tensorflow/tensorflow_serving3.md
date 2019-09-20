## Tensorflow serving 3
### trouble shooting

Evaluation 까지에선 문제없이 돌던 모델이, tensorflow serving 에 올리고 났을때에 에러를 발생시킬때가 있다.

* api 로 해당 model 을 호출했을 때에 아래와 같이 "NodeDef mentions attr 'batch_dims' not in Op" 라는 메시지를 띄우는 경우
```
2019-09-20 09:10:10.315144: E external/org_tensorflow/tensorflow/core/common_runtime/executor.cc:623] Executor failed to create kernel. Invalid argument: NodeDef mentions attr 'batch_dims' not in Op<name=GatherV2; signature=params:Tparams, indices:Tindices, axis:Taxis -> output:Tparams; attr=Tparams:type; attr=Tindices:type,allowed=[DT_INT32, DT_INT64]; attr=Taxis:type,allowed=[DT_INT32, DT_INT64]>; NodeDef: {{node embedding_lookup}} = GatherV2[Taxis=DT_INT32, Tindices=DT_INT64, Tparams=DT_FLOAT, batch_dims=0, _device="/job:localhost/replica:0/task:0/device:GPU:0"](glove/read, _arg_encode_ids_0_0/_35, embedding_lookup/axis). (Check whether your GraphDef-interpreting binary is up to date with your GraphDef-generating binary.).
	 [[{{node embedding_lookup}} = GatherV2[Taxis=DT_INT32, Tindices=DT_INT64, Tparams=DT_FLOAT, batch_dims=0, _device="/job:localhost/replica:0/task:0/device:GPU:0"](glove/read, _arg_encode_ids_0_0/_35, embedding_lookup/axis)]]
2019-09-20 09:38:25.013610: E external/org_tensorflow/tensorflow/core/common_runtime/executor.cc:623] Executor failed to create kernel. Invalid argument: NodeDef mentions attr 'batch_dims' not in Op<name=GatherV2; signature=params:Tparams, indices:Tindices, axis:Taxis -> output:Tparams; attr=Tparams:type; attr=Tindices:type,allowed=[DT_INT32, DT_INT64]; attr=Taxis:type,allowed=[DT_INT32, DT_INT64]>; NodeDef: {{node embedding_lookup}} = GatherV2[Taxis=DT_INT32, Tindices=DT_INT64, Tparams=DT_FLOAT, batch_dims=0, _device="/job:localhost/replica:0/task:0/device:GPU:0"](glove/read, _arg_encode_ids_0_0/_107, embedding_lookup/axis). (Check whether your GraphDef-interpreting binary is up to date with your GraphDef-generating binary.).
	 [[{{node embedding_lookup}} = GatherV2[Taxis=DT_INT32, Tindices=DT_INT64, Tparams=DT_FLOAT, batch_dims=0, _device="/job:localhost/replica:0/task:0/device:GPU:0"](glove/read, _arg_encode_ids_0_0/_107, embedding_lookup/axis)]]

```

이 에러는 model 을 training 시킨 tensorflow version 과 serving에 쓰인 docker image 의 버전이 맞지 않을 때 발생할 수 있다.

나의 경우 tensorflow 1.14.0 에서 training 한 모델을 1.12.0 의 tensorflow serving docker image 에서 돌렸을 경우였고, serving 의 docker 를 최신버전으로 올린 후 해결됐다.