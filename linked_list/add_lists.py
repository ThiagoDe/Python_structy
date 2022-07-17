from node_printer import Node, print_list

#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

def add_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    current_1 = head_1
    current_2 = head_2
    carry = 0

    while current_1 or current_2 or carry == 1:
        val_1 = current_1.val if current_1 else 0
        val_2 = current_2.val if current_2 else 0

        sum = val_1 + val_2 + carry 
        if sum > 9: 
            carry = 1
            sum = sum % 10
        else:
            carry = 0

        tail.next = Node(sum)
        tail = tail.next
        
        if current_1:
            current_1 = current_1.next   
        if current_2:
            current_2 = current_2.next   

    return dummy_head.next.val 
        

        


print(add_lists(a1, b1))
# 5 -> 7 -> 9
