def pair_product(numbers, target_product):
    num_i = {}
    for i, num in enumerate(numbers):
        complement = target_product / num 
        if complement in num_i:
            return (num_i[complement], i)
        else:
            num_i[num] = i 

print(pair_product([3, 2, 5, 4, 1], 8) ) # -> (1, 3)
print(pair_product([3, 2, 5, 4, 1], 10))  # -> (1, 2)
