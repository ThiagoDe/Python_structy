from node_printer import Node 

u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

def is_univalue_list(head, prev = None):
    if head is None:
        return True

    if prev is None or head.val == prev:
        return is_univalue_list(head.next, head.val)
    else:
        return False
    # current = head
    # val = head.val
    # while current:
    #     if current.val != val:
    #         return False
    #     current = current.next

    # return True 

# 2 -> 2 -> 3 -> 3 -> 2

print(is_univalue_list(u))  # False
