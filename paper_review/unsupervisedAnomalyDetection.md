## Unsupervised Anomaly Detection with Generative Adversarial Networks (2017)
### motivation
* 의료 영상 분야에서 병변을 찾아내는 연구
* anomaly detection 을 unsupervised 로 해 보자

### training
* gan train -> 정상 이미지를 내어 놓는 gan 만들기
* 알고 있는 분포(이 분포를 가져온다 라는 부분을 gan 으로 하겠다!)와 다른게 있다면 anomalies 로 인식하겠다

2. mapping new images to the latent space

discrimination loss(real - generated)
f --> (discriminator를 태운 값)

여기서의 discriminator 는 실제 판별하는 역할보다도, feature 추출 역할을 하게 됨


latent space 구성을 위해서 residual loss + discriminate loss 더한 loss 값 이용


anomaly score 도 얘를 똑같이 사용함

https://arxiv.org/abs/1703.05921
https://www.slideshare.net/MingukKang/anomaly-detection-121788059