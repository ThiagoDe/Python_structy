from typing import Counter


def anagrams(s1, s2):
#     return counter(s1) == counter(s2)
    return Counter(s1) == Counter(s2)
# def counter(s):
#     count = {}
#     for char in s:
#         if char not in count:
#             count[char] = 0
#         count[char] += 1
#     return count




print(anagrams('restful', 'fluster'))  # -> True
print(anagrams('cats', 'tocs'))  # -> False
