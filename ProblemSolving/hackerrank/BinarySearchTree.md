## hackerrank - Binary Search Tree
https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees
### problem
```
You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

image 
In the diagram above, the lowest common ancestor of the nodes  and  is the node . Node  is the lowest node which has nodes  and  as descendants.

Function Description

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters: 
- root: a pointer to the root node of a binary search tree 
- v1: a node.data value 
- v2: a node.data value

Input Format

The first line contains an integer, , the number of nodes in the tree. 
The second line contains  space-separated integers representing  values. 
The third line contains two space-separated integers,  and .

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

Constraints

 
 
 
The tree will contain nodes with data equal to  and .

Output Format

Return the a pointer to the node that is the lowest common ancestor of  and .

Sample Input

6
4 2 3 1 7 6
1 7
image

 and .
```

### solution
```python
def lca(root, v1, v2):
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    elif root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    else:
        return root
```