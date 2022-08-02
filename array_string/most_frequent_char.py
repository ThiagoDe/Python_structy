def most_frequent_char(s):
    count = {}
    for char in s:
        count[char] = 1 + count.get(char, 0)
        # if char not in count:
        #     count[char] = 0
        # count[char] += 1
    
    best = None 

    for char in s:
        if best is None or count[char] > count[best]:
            best = char 

    return best 

print(most_frequent_char('mississippi'))  # -> 'i'
