1. 코루틴(coorperative routine)
![coroutine](img/coroutine1.png "coroutine")
- 함수가 종료되지 않은 상태에서 메인 루틴의 코드 실행 후 다시 돌아와서 코루틴 실행
- 종료되지 않았으므로 코루틴 내용도 계속 유지됨
- generator의 특별한 형태인 것 - yield로 값을 받아올 수 있게 함
- 