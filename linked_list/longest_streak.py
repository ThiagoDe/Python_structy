from node_printer import Node

a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def longest_streak(head):
    max_streak = 0
    current_streak = 0
    prev_val = None
    current_node = head
    while current_node:
        if current_node.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1

        prev_val = current_node.val
        if current_streak > max_streak:
            max_streak = current_streak

        current_node = current_node.next

    return max_streak

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longest_streak(a))  # 3
