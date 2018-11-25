## save numpy to npy file
```python
import numpy as np
data = np.arange(100) # 저장하는 데이터
np.save('my_data.npy', data) # numpy.ndarray 저장. @파일명, @값
data2 = np.load('my_data.npy') # 데이터 로드. @파일명
```

