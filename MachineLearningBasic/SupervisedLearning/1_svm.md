
	• Classification error --> svm 의 error function 은 조금 더 까다로워
		○ Margin line 을 더 그려(wx+b=1 , wx+b=-1)
		○ 이 거리를 같이 둔 상태로 error function 을 적용해(error 가 전보다 더 커지겠지)
	• Margin error
		○ 마진을 error 로 만들고 싶어(gradient descent 로 minimize 하고싶거든) --> 이런 error function 을 만들거야
			§ Error function : 우리는 large margin 에 대해서 적은 에러를 내고, small margin 에 대해서 많은 에러를 내는 함수를 찾을거야
			§ 왜냐면 되도록이면 큰 마진을 만들어내는게 안정적인 classification function 을 찾는거니까
		○ Margin = 2/|w|
		○ --> error=|w|^2(w는 vecrtor니까 --> w1^2+w2^2
		○ --> 마진이 크면 에러는 작아지고, 마진이 작으면 에러는 커져
