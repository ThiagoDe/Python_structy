from node_tree import Node

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
def max_path_sum(root):
    if root is None: return 0
    max_path = max(max_path_sum(root.left), max_path_sum(root.right))
    return root.val + max_path

print(max_path_sum(a))  # -> 18
