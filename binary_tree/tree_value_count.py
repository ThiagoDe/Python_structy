from node_tree import Node
from collections import deque

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12
def tree_value_count(root, target):
    total_times = 0
    queue = deque([ root ])
    while queue:
        current = queue.popleft()
        if current.val == target: total_times += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return total_times


# def tree_value_count(root, target):
#   if root is None:
#       return 0
#   total = 1 if root.val == target else 0
#   return total + tree_value_count(root.left, target) + tree_value_count(root.right, target)


print(tree_value_count(a,  6))  # -> 3
