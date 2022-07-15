def compress(s):
    s += '!' # add char so the last is different and trigers the else to append 
    i = 0
    j = 0
    restult = []

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i 
            if num > 1:
                restult.append(str(num))
                restult.append(s[i])
            else:
                restult.append(s[i])

            i = j
    return ''.join(restult)


print(compress('ccaaatsss'))  # -> '2c3at3s'
