def intersection(a, b):
    set_items = set(a)
    # result = []
    # for el in b:
    #     if el in set_items:
    #         result.append(el)

    val = [ el for el in b if el in set_items]
    return sorted(val)

print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
print(intersection([2,4,6], [4,2])) # -> [2,4]