## leetcode - Container With Most Water
### problem
https://leetcode.com/problems/container-with-most-water/
```
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

### solution
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        list_size=len(height)
        max_area=0

        l=0
        r=list_size-1
        while l<r:
            new_area=(r-l)*min(height[l], height[r])
            if max_area< new_area:
                max_area=new_area

            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
                
        return max_area
```