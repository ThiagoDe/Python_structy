def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    
    best = None 

    for chat in s:
        if best is None or count[char] > count[best]:
            best = char 

    return best 

print(most_frequent_char('mississippi'))  # -> 'i'
