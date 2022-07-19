from node_tree import Node

a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3
def leaf_list(root, leaves = []):
    if root is None: return []
    if root.left is None and root.right is None:
        leaves.append(root.val)
    leaf_list(root.left, leaves)
    leaf_list(root.right, leaves)
    return leaves
    

print(leaf_list(a))  # -> [ 20, 1, 3, 54 ]
