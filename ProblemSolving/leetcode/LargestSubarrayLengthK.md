## Largest Subarray Length K
### problem
```
Array X is greater than array Y if the first non-matching element in both arrays has a greater value in X than in Y.
For example, for arrays X and Y such that:
x=[1,2,3,4,5]
y=[1,2,4,3,5]
Y is greater than X because the first element that does not match is larger in Y(i.e. for x[2] and y[2], x[2]<y[2]).
A contiguous subarray is defined by an interval of the indices. In other words, a contiguous subarray is a subarray which has consecutive indexes.
Write a function that, given a zero-indexed array A consisting of N integers and an integer K, returns the largest contiguous subarray of length K from all the contiguous subarrays of length K.

For example, given array A and K=4 such that: 
A=[1,4,3,2,5]
the function should return [4,3,2,5], because there are two subarrays of size 4:
[1,4,3,2]
[4,3,2,5]
and the largest subarray is [4,3,2,5]
Assume that:
1<=K<=N<=100
1<=A[J]<=1000
given an array A contains N distinct integers.

In your solution, focus on correctness. The performance of your solution will not be the primary focus of the assessment.
```
### solution1
```python
def compare_string(A, k):
	def get_len(arr1, arr2):
	    for i in range(len(arr1)):
	        if arr1[i]!=arr2[i]:
	            if arr1[i]>arr2[i]:
	                return (arr1[i], arr1)
	            else:
	                return (arr2[i], arr2)
	max_arr=[]
	max_len=0
	for i in range(len(A)-k+1):
	    print(i)
	    crr=A[i:i+k]
	    if len(max_arr)==0:
	        max_arr=crr
	        continue
	    max_arr, max_len=get_len(max_arr, crr)
	return max_arr
```
### solution2
- A 에 들어가는 integer 가 distinct 라고 했으니 그냥 맨 앞에 숫자가 제일큰 subarray 를 구하면 된다;;
```python
def compare_string(A, k):
	max_len=max(A[:len(A)-k+1])
	index=A.index(max_len)
	return A[index:index+k]
```