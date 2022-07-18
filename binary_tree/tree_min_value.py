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
def tree_min_value(root):
    queue = deque([ root ])
    min = float('inf')
    while queue:
        current = queue.popleft()
        if current.val < min: min = current.val

        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return min 


# def tree_min_value(root):
#   if root is None:
#       return float('inf')
#   min_val = min(root.val, tree_min_value(
#       root.left), tree_min_value(root.right))
#   return min_val

print(tree_min_value(a))  # -> -2
