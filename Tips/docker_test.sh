docker run -p 8501:8501   --mount type=bind,  source=/tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu,  target=/models/half_plus_two   -e MODEL_NAME=half_plus_two -t tensorflow/serving &

docker run -p 8501:8501 \
  --mount type=bind,source=/path/to/my_model/,target=/models/my_model \
  -e MODEL_NAME=my_model -t tensorflow/serving


tensorflow_model_server --port=8500 --rest_api_port=8501 \
  --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME}


docker run -p 8501:8501 \
--mount type=bind , \
source=/tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu, \
target=/models/half_plus_two\
-e MODEL_NAME=half_plus_two -t tensorflow/serving


tensorflow_model_server --port=8500 --rest_api_port=8501 \
  --model_name=half_plus_two --model_base_path=/tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu


docker run -it -v /:/myroot alpine /bin/sh -c "mkdir -p /myroot/etc/mysql/scripts/"

docker cp /tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu serving_base:/models/half_plus_two


docker commit --change "ENV MODEL_NAME half_plus_two" serving_base half_plus_two


docker run -p 8501:8501 half_plus_two

aa-rec-gpu01.dakao.io


3c52fd0c6f60
578d433315ea

docker cp /tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu serving_base:/models/half_plus_two

python_deployer.deploy_python_closure(clipper_conn, name="sum-model", version=3, input_type="doubles", func=feature_sum)


NV_GPU=7 nvidia-docker run --memory="512m" -p 8501:8501 half_plus_two_gpu

--memory="1g" --memory-swap="2g"