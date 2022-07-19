from node_tree import Node

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
def all_tree_paths(root):
    if root is None: return []
    if root.left is None and root.right is None:
        return [ [ root.val ] ]
    paths = []

    left = all_tree_paths(root.left)
    for sub in left:
        paths.append([root.val, *sub])
    right = all_tree_paths(root.right)
    for sub in right:
        paths.append([root.val, *sub])

    return paths

print(all_tree_paths(a))  # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]
