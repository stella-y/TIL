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
