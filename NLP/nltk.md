## NLTK
1. 영어 corpus download
소설, 신문 등의 문서 / 품사, 형태소등의 구조적 형태로 정리해둔것도 포함
```python
import nltk
nltk.download('book', quiet=True)
from nltk.book import *
```
구텐베르크 말뭉치 
```python
nltk.corpus.gutenberg.fileids()
emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
print(emma_raw[:1302])
'''
['austen-emma.txt',
 'austen-persuasion.txt',
 'austen-sense.txt',
 'bible-kjv.txt',
 'blake-poems.txt',
 'bryant-stories.txt',
 'burgess-busterbrown.txt',
 'carroll-alice.txt',
 'chesterton-ball.txt',
 'chesterton-brown.txt',
 'chesterton-thursday.txt',
 'edgeworth-parents.txt',
 'melville-moby_dick.txt',
 'milton-paradise.txt',
 'shakespeare-caesar.txt',
 'shakespeare-hamlet.txt',
 'shakespeare-macbeth.txt',
 'whitman-leaves.txt']
 '''
 '''
[Emma by Jane Austen 1816]

VOLUME I

CHAPTER I


Emma Woodhouse, handsome, clever, and rich, with a comfortable home
and happy disposition, seemed to unite some of the best blessings
of existence; and had lived nearly twenty-one years in the world
with very little to distress or vex her.
 '''
```

2. 토큰 생성(tokenizer 제공)
```python
from nltk.tokenize import sent_tokenize
print(sent_tokenize(emma_raw[:1000])[3])
'''Sixteen years had Miss Taylor been in Mr. Woodhouse's family,
less as a governess than a friend, very fond of both daughters,
but particularly of Emma.'''
from nltk.tokenize import word_tokenize
word_tokenize(emma_raw[50:100])
'''['Emma',
 'Woodhouse',
 ',',
 'handsome',
 ',',
 'clever',
 ',',
 'and',
 'rich',
 ',',
 'with',
 'a']'''
from nltk.tokenize import RegexpTokenizer
retokenize = RegexpTokenizer("[\w]+")
retokenize.tokenize(emma_raw[50:100])
'''['Emma', 'Woodhouse', 'handsome', 'clever', 'and', 'rich', 'with', 'a']'''
```

3. 형태소분석
stemming, lemmatizing, pos tagging

https://datascienceschool.net/view-notebook/118731eec74b4ad3bdd2f89bab077e1b/