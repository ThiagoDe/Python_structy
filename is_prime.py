from math import sqrt, floor 

def is_prime(n):
    if n < 2:
      return False

    for x in range(2, floor(sqrt(n)) + 1):
        if n % x == 0:
            return False 

    return True

print(is_prime(3)) # -> True

print(is_prime(4)) # -> False