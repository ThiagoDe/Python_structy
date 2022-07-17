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

def depth_first_values(root):
    # if root is None:
    #     return []
    # stack = [ root ]
    # values = []
    # while stack:
    #     current = stack.pop()
    #     values.append(current.val)

    #     if current.right:
    #         stack.append(current.right)
    #     if current.left:
    #         stack.append(current.left)

    # return values
    if root is None:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]


print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
