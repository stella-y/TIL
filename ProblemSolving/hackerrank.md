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