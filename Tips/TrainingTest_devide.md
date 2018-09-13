### training test set 분리 법

* numpy - randn

``` python 
df = pd.DataFrame(np.random.randn(100, 2))
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
```

* scikit learn - train_test_split

``` python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.2)
```

* pandas - random sample

``` python
train=df.sample(frac=0.8,random_state=200)
test=df.drop(train.index)
```