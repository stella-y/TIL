## hackerrank
### Tree: Level Order Traversa
https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
```python
import queue
def levelOrder(root):
    #Write your code hereimport queue
    q=queue.Queue()
    q.put(root)
    
    while q.qsize()>0:
        node=q.get()
        print(node.info, end=' ')
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
```

### Balanced Brackets
https://www.hackerrank.com/challenges/balanced-brackets/problem
```python
def isBalanced(s):
    start=['[','{','(']
    end=[']','}', ')']
    stack=[]
    for e in s:
        if e in start:
            stack.append(e)
        elif e in end:
            if len(stack)<=0:
                return "NO"
            p=stack.pop()
            if start.index(p)==end.index(e):
                pass
            else:
                return "NO"
        else:
            return "NO"
    if len(stack)>0:
        return "NO"
    else:
        return "YES"
```

## Find the Running Median
https://www.hackerrank.com/challenges/find-the-running-median/problem
```python
import bisect
def runningMedian(a):
    #
    # Write your code here.
    #
    sorted_list=[]
    ans_list=[]
    for x in a:
        bisect.insort(sorted_list, x)
        len_list=len(sorted_list)
        if len_list%2==1:
            med_idx=int(len_list/2)
            ans_list.append(sorted_list[med_idx])
        else:
            med_idx=int(len_list/2)
            ans_list.append((sorted_list[med_idx-1]+sorted_list[med_idx])/2)

    return ans_list
```