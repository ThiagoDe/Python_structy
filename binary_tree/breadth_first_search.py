from node_tree import Node
from collections import deque

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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
def breadth_first_values(root):
    if root is None: return []
    queue = deque([ root ])
    values = []
    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return values 



print(breadth_first_values(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
