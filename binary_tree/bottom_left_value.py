from node_tree import Node
from collections import deque

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \
#    -2  6

def bottom_right_value(root):
    queue = deque([ root ])
    last = root.val
    while queue:
        current = queue.popleft()
        last = current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return last

print(bottom_right_value(a))  # -> 6
