
docker rm $(docker ps -a | grep Exited | grep half_plus_two | awk '{print $1}')



docker rm $(docker ps -a | grep query_frontend | awk '{print $1}')
docker rm $(docker ps -a | grep Exited | grep redis | awk '{print $1}')
docker rm $(docker ps -a | grep Exited | grep metric_frontend | awk '{print $1}')

docker rm $(docker ps -a | grep Exited | grep mgmt_frontend | awk '{print $1}')


docker rm $(docker ps -a --no-trunc | grep Exited | grep clipper | awk '{print $1}')

docker rm $(docker ps -a --no-trunc | grep Exited | grep sum-model_1 | awk '{print $1}')

docker rm $(docker ps -a --no-trunc | grep Exited | grep query_frontend | awk '{print $1}')





docker rmi -f $(docker images | grep default-cluster-sum-model | awk '{print $3}')
docker rmi -f $(docker images | grep redis | awk '{print $3}')
docker rmi -f $(docker images | grep clipper | awk '{print $3}')
docker rmi -f $(docker images | grep prometheus | awk '{print $3}')









docker rmi $(docker images | grep default-cluster-sum-model )
redis
clipper
prometheus

