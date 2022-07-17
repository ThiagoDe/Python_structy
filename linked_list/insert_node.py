from node_printer import Node, print_list

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
def insert_node(head, value, index):
    if index == 0:
        node = Node(value)
        node.next = head 
        return node 

    current = head 
    while current:
        if index == 1:
            next_node = current.next 
            current.next = Node(value)
            current.next.next = next_node
            return head
        index -= 1
        current = current.next 
        


print_list(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d
