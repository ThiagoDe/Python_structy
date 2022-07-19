from node_tree import Node
from collections import deque

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i
def tree_levels(root):
    queue = deque([ [root, 0] ])
    paths = []
    while queue:
        node, level = queue.popleft()
        if len(paths) == level:
            paths.append([ node.val ])
        else:
            paths[level].append(node.val)

        if node.left:
            queue.append([node.left, level + 1])
        
        if node.right:
            queue.append([node.right, level + 1])

    return paths 

print(tree_levels(a))  # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]
