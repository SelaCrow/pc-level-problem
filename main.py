# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# import deque (not required to use, but may be helpful)
from collections import deque

def level(root):
    if root is None:
        return -1

    # queue for BFS, starting with the root
    queue = deque([root])

    # keeps track of which level we’re on
    current_level = 0

    # track the level with the most nodes seen so far
    max_nodes = 0
    max_level = 0

    # standard BFS loop
    while queue:
        # number of nodes at *this* level
        level_size = len(queue)

        # if this level beats the previous max, update it
        if level_size > max_nodes:
            max_nodes = level_size
            max_level = current_level

        # process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()


r"""
             1
           /    \
          /      \
         2        3
       /   \    /   \
      4     5  6     7
     / \      / \
    8   9    10 11
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
assert level(root) == 2

r"""
    1
"""
root = Node(1)
assert level(root) == 0

r"""
             1
           /   \
          /     \
         2       3
       /   \
      4     5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
assert level(root) == 1

r"""
    Empty Tree
"""
root = None
assert level(root) == -1

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
