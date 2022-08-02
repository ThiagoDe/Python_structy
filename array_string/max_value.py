def max_value(nums):
    max = float('-inf')

    for n in nums:
        # max = max(max, n)
        if n > max:
            max = n 

    return max 

print(max_value([4, 7, 2, 8, 10, 9])) # -> 10
    
