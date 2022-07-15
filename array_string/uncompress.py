def uncompress(s):
    numbers = '1234567890'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j 

    return ''.join(result)




print(uncompress("2c3a1t")) # -> 'ccaaat'