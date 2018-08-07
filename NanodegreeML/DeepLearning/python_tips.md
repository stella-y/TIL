* python naming convention
  * module_name, package_name, ClassName, method_name, ExceptionName, function_name
  * GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
* package
  ``` 
  game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
  ```
  * __init__.py
    * __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할
    - 만약 game, sound, graphic등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식이 안됨
    (python3.3 버전부터는 __init__.py 파일 없이도 패키지로 인식이 된다(PEP 420). 
    하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.)
    특정 디렉터리의 모듈을 *를 이용하여 import할 때에는 다음과 같이 해당 디렉터리의 __init__.py 파일에 __all__이라는 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.
  * __all__
    ``` python
    __all__ = ['echo']
    ```
    * __all__이 의미하는 것은 타 디렉터리에서 * 기호를 이용하여 import할 경우 이곳에 정의된 echo 모듈만 import된다는 의미
    (착각하기 쉬운데 from game.sound.echo import * 는 __all__과 상관없이 무조건 import된다. 이렇게 __all__과 상관없이 무조건 import되는 경우는 from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우)
  * relative package
    * 만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면
      ``` python
      # render.py
      from game.sound.echo import echo_test
      ```
      ``` python
      from ..sound.echo import echo_test
      ```
* Python stype guide
 * https://www.python.org/dev/peps/pep-0008/
 
* 예외처리
 1. try, except만 쓰는 방법
  ``` python
  try:
    ...
  except:
    ...
  ```
    이 경우는 오류 종류에 상관없이 오류가 발생하기만 하면 except 블록을 수행한다.
  2. 발생 오류만 포함한 except문
   ``` python 
   try:
    ...
   except 발생 오류:
    ...
   ```
   이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다.
  3. 발생 오류와 오류 메시지 변수까지 포함한 except문
   ``` python
   try:
    ...
   except 발생 오류 as 오류 메시지 변수:
    ...
   ```
   이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.
   이 방법의 예를 들어 보면 다음과 같다.
   ``` python
    try:
        4 / 0
    except ZeroDivisionError as e:
        print(e)
   ```
   * blas 
       * basic linear algebra system
       * 벡터 및 행렬 연산을 관장하는 스펙 
       * GNU Octave2, Mathematica, NumPy, R, 그리고 아래의 LAPACK 등 다양한 소프트웨어에 사용된다. BLAS를 잘 설정하고 다루면 같은 코드를 돌리더라도 몇 배에 달하는 속도 향상을 이룰 수 있기 때문에 잘 이해하고 있으면 좋다
       * Blas 구현체
           * NVIDIA의 CUDA용 cuBLAS, AMD의 ACML, 인텔의 MKL, 애플의 Accelerate Framework안에 포함된 vecLib, 오픈소스인 ATLAS, 그리고 아마 가장 범용적으로 쓰이는 오픈소스 OpenBLAS 등이 있으며 그 외에도 다양한 구현체가 있다.
           https://www.lucypark.kr/blog/2015/09/06/blas-benchmarks/
       * benchmark test 해보고 성능향상할 부분 있으면 해둬야
       
