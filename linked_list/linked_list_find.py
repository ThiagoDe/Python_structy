from node_printer import Node

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d


# def linked_list_find(head, target):
#   if head.val == target:
#     return True
#   if head.next:
#     return linked_list_find(head.next, target)

#   return False


def linked_list_find(head, target):
    current = head 
    while current:
        if current.val == target:
            return True
        current = current.next
    return False

print(linked_list_find(a, "c"))  # True