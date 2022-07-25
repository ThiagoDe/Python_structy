def linked_list_cycle(head):
    visited = set()
    current = head
    while current:
        if current.val in visited: return True 
        visited.add(current.val)
        current = current.next

    return False 