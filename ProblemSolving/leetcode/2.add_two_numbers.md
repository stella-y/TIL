## leetcode -add two numbers
### problem
https://leetcode.com/problems/add-two-numbers/
```
Add two numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself
```

### solution
```python
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry=0
        head=None
        last=None

        while(l1 or l2):
            
            if l1 is None:
                tmp=l2.val+carry
            elif l2 is None:
                tmp=l1.val+carry
            else:
                tmp=l1.val+l2.val+carry
            carry =int(tmp/10)

            new_node=ListNode(tmp-carry*10)
            if head:
                last.next=new_node
                last=new_node
            else:
                head=new_node
                last=new_node
            
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        if carry !=0:
            new_node=ListNode(1)
            last.next=new_node
            
        return head

```