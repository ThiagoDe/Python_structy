from node_printer import Node, print_list

def create_linked_list(values, i = 0):
    # tail = Node(None)
    # current = tail 
    # for val in values:
    #     current.next = Node(val)     
    #     current = current.next 
    
    # return tail.next
  if i == len(values):
    return None

  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head

# print_list(create_linked_list(["h", "e", "y"]))
# h -> e -> y
print_list(create_linked_list([1, 7, 1, 8]))
# 1 -> 7 -> 1 -> 8
