from node_printer import Node

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def get_node_value(head, index):
    # current = head 
    # while current:
    #     if index == 0:
    #         return current.val
    #     index -= 1
    #     current = current.next

    # return None
    if head is None:
        return None  
    if index == 0:
        return head.val
    return get_node_value(head.next, index - 1)
    

# a -> b -> c -> d

print(get_node_value(a, 2))  # 'c'
