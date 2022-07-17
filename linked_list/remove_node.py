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

def remove_node(head, target_val):
    # tail = Node(None)
    # tail.next = head 
    # current = tail
    # while current.next:
    #     if current.next.val == target_val:
    #         current.next = current.next.next
    #         break
    #     current = current.next 

    # return tail.next 
  if head.val == target_val:
    return head.next

  current = head 
  prev = None 
  while current:
    if current.val == target_val:
      prev.next = current.next 
      break
    else:
      prev = current
      current = current.next 
      
  return head    

# a -> b -> c -> d -> e -> f

print_list(remove_node(a, "c"))
# a -> b -> d -> e -> f
