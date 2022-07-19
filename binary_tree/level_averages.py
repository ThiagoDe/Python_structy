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
def level_averages(root):
    queue = deque([(root, 0)])
    averages = []
    while queue:
        node, level = queue.popleft()
        if len(averages) == level:
            averages.append([ node.val ])
        else:
            averages[level].append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        
        if node.right:
            queue.append((node.right, level + 1))

    results = []   
    for sub_levels in averages:
        results.append(sum(sub_levels) / len(sub_levels))

    return results

print(level_averages(a))  # -> [ 3, 7.5, 1 ]
