from node_tree import Node
from collections import deque

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
def path_finder(root, target):
    result = _path_finder(root, target)
    if result is None:
        return None
    else:
        return result[::-1]

def _path_finder(root, target):
    if root is None: return None
    if root.val == target: 
        return [ root.val ]
    
    left = _path_finder(root.left, target)
    if left: 
        left.append(root.val)
        return left 
    right = _path_finder(root.right, target)
    if right:
        right.append(root.val)
        return right 

    return None

print(path_finder(a, 'e'))  # -> [ 'a', 'b', 'e' ]
