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
    # if index == 0:
    #     node = Node(value)
    #     node.next = head 
    #     return node 

    # current = head 
    # while current:
    #     if index == 1:
    #         next_node = current.next 
    #         current.next = Node(value)
    #         current.next.next = next_node
    #         return head
    #     index -= 1
    #     current = current.next 
  if index == 0:
    new_node = Node(value)
    new_node.next = head
    return new_node

  if head is None:
    return Node

  if index == 1:
    temp = head.next
    head.next = Node(value)
    head.next.next = temp
    return

  insert_node(head.next, value, index - 1)
  return head
        


print_list(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d
