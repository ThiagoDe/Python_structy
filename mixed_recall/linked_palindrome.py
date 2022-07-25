def linked_palindrome(head):
    val = []
    current = head
    while current:
        val.append(current.val)
        current = current.next 

    return val == val[::-1]