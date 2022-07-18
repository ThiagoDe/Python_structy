from node_tree import Node
from collections import deque 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g
def how_high(root):
    if root is None: return -1
    return 1 + max(how_high(root.left), how_high(root.right))
        
        

print(how_high(a))  # -> 3
