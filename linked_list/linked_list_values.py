from node_printer import print_list, Node


def linked_list_values(head):
    l = []
    current = head
    while current:
        l.append(current.val)
        current = current.next
        
    return l

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

  # -> [ 'a', 'b', 'c', 'd' ]
print(linked_list_values(a))
