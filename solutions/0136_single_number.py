# https://leetcode.com/problems/single-number/


# type: ignore
from collections import Counter


# T: O(n)
# S: O(1)
class Solution:
    def singleNumber(self, numbers: list[int]) -> int:
        x = 0
        for number in numbers:
            x ^= number
        return x


# T: O(n)
# S: O(n)
# class Solution:
#     def singleNumber(self, numbers: list[int]) -> int:
#         counter = Counter(numbers)
#         for number in counter:
#             if counter[number] == 1:
#                 return number
#         raise
