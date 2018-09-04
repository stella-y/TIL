	• 개발 배경 - 번역기 런칭하고나서 해보고싶어짐
		○ 해보겠다고 하니깐 하게 해주신
	• Testing is all you need - 짱 중요하다
	• 모델 학습시키는데 데이터 반 정도 돌다가 죽는 경우
		○ Batch size 로 데이터가 안나눠떨어져서
	• 데이터도 모델도 이상이 없는데 결과가 이상하게 나옴
		○ Test case를 만들어봤으면 괜찬ㄴㅎ았을텐뎅…
	• 텐서플로 - 그래프 그리고나서 데이터 흘리는 방식이지요
	• Tf.print - 그래프 안에 프린트하는 노드를 만드는 것
		○ 돌다가 죽으면 빨리 찍어내고 싶어질때
	• Unit test
		○ Tf.test.testcase쓰면 unit test 만들 수있어


## dataset
	• 난이도별 , 단계별 데이터 셋을 각각 만들어놓음 
	• 모듈 변경할때마다 가장 기본 데이트부터 다시 돌려봄 

## 모델 구조 및 데이터 변경하던 과정
	• GitHub issue 에 등록해서 씀
	• Git branch 따서 후보 모델 막 생성해서 cloud 사용해서 튜닝함
	• 여기서 모델 등록부터 텐서보드까지 다 지원하나봐 

# 모델 측면
## 
	• CNN
		○ 사람의 뇌도 대각선에 잘 반응하는 뉴런 이런것들이 따로 있음
		○ 이걸 도와주는데 CNN
		○ Feature extraction
	• 이 위에 RNN layer 쌓음(lstm)
		○ 수용장 자체를 세로로 길쭉하게 만듦
		○ Broaden the receptive fields
		○ 이전의 그림까지 가져와서 학습시키기 위해서 RNN 쓴 것
	• Ctc algorithm
		○ 이미지가 들어왔을 떄에 글자가 나올 확률을 높여주는 역할
		○ Encoding —> 반복되는 글자 합치기 —> 빈칸 지우기
		○ 이게 라스가 썼던건가?
		○ 여기서 목적함수로
	• Ctc의 약점
		○ Conditional independence assumption
		○ Pooling size 제한
	• Lstm 
		○ 속도가 짱 느려(병렬로 쓸수가 없으니깐)


## 약점 보완하기
	• Lstm —> encoder decoder with attention 으로
	• Self-attention - 하나의 cell 에 여러 정보를 담을 수 있게
	• 근데 일케하니깐 정확도가 쭉 떨어졌댕

##
