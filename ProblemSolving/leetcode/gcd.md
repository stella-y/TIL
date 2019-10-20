```python
def gcd (a, b):
	if a==0:
		return b
	if b==0:
		return a
	if a==b:
		return a

	if a> b:
		return gcd(a-b, b)
	return gcd(b-a, a)
```
```python
def gcd(a, b):
	while a>0 and b>0 and a!=b:
		if a>b:
			a=a-b
		elif a<b:
			b=b-a
	if a==0 or a==b:
		return b
	if b==0:
		return a
```