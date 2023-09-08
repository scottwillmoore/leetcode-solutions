# https://leetcode.com/problems/single-number/


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
#         counts: dict[int, int] = {}
#
#         for number in numbers:
#             if number in counts:
#                 counts[number] += 1
#             else:
#                 counts[number] = 1

#         for number in counts:
#             if counts[number] == 1:
#                 return number

#         raise
