from node_printer import Node, print_list

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

def merge_lists(head_1, head_2):
    dummyHead = Node(None)
    tail = dummyHead
    current_1 = head_1
    current_2 = head_2
    while current_1 and current_2:
        if current_1.val < current_2.val:
            dummyHead.next = current_1
            current_1 = current_1.next
        else:
            dummyHead.next = current_2
            current_2 = current_2.next 
        dummyHead = dummyHead.next 

    if current_1:
        dummyHead.next = current_1

    if current_2:
        dummyHead.next = current_2 
            
    return tail.next 
        
print_list(merge_lists(a, q))
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
