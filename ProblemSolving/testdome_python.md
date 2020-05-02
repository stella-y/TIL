1. File Owners
- problem
```
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
```
- solution
```python
import collections

def group_by_owners(files):
    ans=collections.defaultdict(list)
    for f in files.keys():
        ans[files[f]].append(f)
    return ans

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }    
    print(group_by_owners(files))
```
2. Quadratic Equation
- problem
```
Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.

The roots of the quadratic equation can be found with the following formula: A quadratic equation.

For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.
```
- solution
```python
import math
def find_roots(a, b, c):
    ans=[]
    mid=math.sqrt(b**2-4*a*c)/(2*a)
    #print(mid)

    ans.append((-b/(2*a))+mid)
    ans.append((-b/(2*a))-mid)
    return tuple(ans)


print(find_roots(1, 2, 1));
```
3. Binary Search Tree
- problem
```
Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.

Write a function that, efficiently with respect to time used, checks if a given binary search tree contains a given value.

For example, for the following tree:

n1 (Value: 1, Left: null, Right: null)
n2 (Value: 2, Left: n1, Right: n3)
n3 (Value: 3, Left: null, Right: null)
Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
```
- solution
```python
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root.value==value:
        return True
    elif root.value < value:
        if root.right:
            #print("right")
            return contains(root.right, value)
        else:
            return False
    elif root.value > value:
        if root.left:
            return contains(root.left, value)
        else:
            return False


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
```
4. Song
- problem
```
A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.

Implement a function is_repeating_playlist that, efficiently with respect to time used, returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.

first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())
```
- solution
```python
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        next_song=self.next
        dict=set(self.name)
        while next_song:
            if next_song.name in dict:
                return True
            else:
                dict.add(next_song.name)
            next_song = next_song.next
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())
```
5. Two Sum
- problem
```
Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return None.

For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:

0 and 3 (or 3 and 0) as 3 + 7 = 10
1 and 5 (or 5 and 1) as 1 + 9 = 10
2 and 4 (or 4 and 2) as 5 + 5 = 10
```
- solution
```python
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    dict={}
    for i, n in enumerate(numbers):
        if n in dict:
            return (i, dict[n])
        else:
            dict[target_sum-n]=i

    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
```
6. League Table
- problem
```
The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 

The player's rank in the league is calculated using the following logic:

The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
If two players are tied on score, then the player who has played the fewest games is ranked higher.
If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.
Implement the player_rank function that returns the player at the given rank.

For example:

table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))
All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".
```
- solution
```python
from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        mid=sorted(self.standings, key=lambda x: self.standings[x].get('games_played'))
        return sorted(mid, key=lambda x : self.standings[x].get('score'), reverse=True)[rank-1]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
```
7. Sorted Search
- problem
```
Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.
```
- solution
```python
import bisect

def count_numbers(sorted_list, less_than):
    return bisect.bisect_left(sorted_list, less_than)

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2
```
8. Train Composition
- problem
```
A TrainComposition is built by attaching and detaching wagons from the left and the right sides, efficiently with respect to time used.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.
```
- solution
```python
import collections
class TrainComposition:
    
    def __init__(self):
        self.deque=collections.deque([])
    
    def attach_wagon_from_left(self, wagonId):
        self.deque.appendleft(wagonId)
    
    def attach_wagon_from_right(self, wagonId):
        self.deque.append(wagonId)

    def detach_wagon_from_left(self):
        return self.deque.popleft()
    
    def detach_wagon_from_right(self):
        return self.deque.pop()

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13
```
9. Route Planner
- problem
```

```
- solution
```python

```

