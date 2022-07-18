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

def tree_includes(root, target):
    if root is None: return False
    # if root.val == target: return True
    # return tree_includes(root.left, target) or tree_includes(root.right, target)
    queue = deque([ root ])
    while queue:
        current = queue.popleft()
        if current.val == target: return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return False
    

print(tree_includes(a, "e"))  # -> True
