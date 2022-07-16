class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    current = head
    list = []
    while current:
        list.append(current.val)
        current = current.next

    print(' -> '.join(list)) 
