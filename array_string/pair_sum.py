def pair_sum(numbers, target_sum):
    num_i = {}
    for i, num in enumerate(numbers):
        dif = target_sum - num
        if dif in num_i:
            return (num_i[dif], i)
        else:
            num_i[num] = i 
        



print(pair_sum([3, 2, 5, 4, 1], 8))  # -> (0, 2)
print(pair_sum([4, 7, 9, 2, 5, 1], 5))  # -> (0, 5)
