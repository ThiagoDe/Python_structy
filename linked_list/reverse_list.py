from node_printer import Node, print_list

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def reverse_list(head, prev = None):
    # current = head  
    # prev = None  
    # while current:
    #     nextNode = current.next
    #     current.next = prev
    #     prev = current
    #     current = nextNode 

    # return prev
    if head is None:
        return prev 
    nextNode = head.next
    head.next = prev 
    return reverse_list(nextNode, head)



# a -> b -> c -> d -> e -> f
# c    n 
print_list(reverse_list(a))  # f -> e -> d -> c -> b -> a
