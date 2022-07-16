from node_printer import Node, print_list

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

def zipper_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None 

    if head_1 is None:
        return head_2

    if head_2 is None:
        return head_1

    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)
    return head_1

    # if head_1 is None and head_2 is None:
    #     return None
    # if head_1 is None:
    #     return head_2
    # if head_2 is None:
    #     return head_1
    # next_1 = head_1.next
    # next_2 = head_2.next
    # head_1.next = head_2
    # head_2.next = zipper_lists(next_1, next_2)
    # return head_1    
    
    # tail = head_1 # a, x, 
    # current_1 = head_1.next # a, b
    # current_2 = head_2 # x
    # count = 0
    # while current_1 and current_2:
    #     if count % 2 == 0:
    #         tail.next = current_2 
    #         current_2 = current_2.next 
    #     else:
    #         tail.next = current_1
    #         current_1 = current_1.next 
    #     tail = tail.next
    #     count += 1

    # if current_1:
    #     tail.next = current_1
    # if current_2:
    #     tail.next = current_2
    # return head_1

print_list(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z
