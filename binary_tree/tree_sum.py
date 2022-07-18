import queue
from node_tree import Node
from collections import deque

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

def tree_sum(root):
    if root is None: return 0
    # return root.val + tree_sum(root.left) + tree_sum(root.right)
    queue = deque([ root ])
    sum = 0
    while queue:
        current = queue.popleft()
        sum += current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return sum
print(tree_sum(a))  # -> 21
