from node_printer import print_list, Node
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None 

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d 

# def print_list(head):
#     current = head
#     list = []
#     while current:
#         list.append(current.val)
#         current = current.next 

#     return ' -> '.join(list)

# print(print_list(a))
print_list(a)