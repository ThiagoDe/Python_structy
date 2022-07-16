from node_printer import Node, print_list

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def sum_list(head):
    current = head 
    sum = 0
    while current:
        sum += current.val
        current = current.next 

    return sum 
    
# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19
