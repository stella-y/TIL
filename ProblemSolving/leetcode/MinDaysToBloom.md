## leetcode - min days to bloom
### problem
```
Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.
```
### solution
```python
def minDaysToBloom(k, n, roses):
    def check(k, n, m, roses):
        i=0
        bouquet=0
        while i<len(roses)-n:
            if max(roses[i:i+n])<=m:
                bouquet+=1
                i=i+n
            else:
                i+=1
        if bouquet >= k:
            return True
        else:
            return False
    l=min(roses)
    r=max(roses)
    while l<=r:
        m=(l+r)//2
        if check(k, n, m, roses):
            r=m-1
        else:
            l=m+1
    return l
```