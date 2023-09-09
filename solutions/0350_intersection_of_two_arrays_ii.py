# https://leetcode.com/problems/intersection-of-two-arrays-ii/


from collections import Counter


# T: O(n)
# S: O(n)
class Solution:
    def intersect(self, a: list[int], b: list[int]) -> list[int]:
        counter = Counter(b)
        c: list[int] = []
        for n in a:
            if counter[n] > 0:
                c.append(n)
                counter[n] -= 1
        return c


# T: O(n log n)
# S: O(n)
# class Solution:
#     def intersect(self, a: list[int], b: list[int]) -> list[int]:
#         a = sorted(a)
#         b = sorted(b)
#         c: list[int] = []

#         i = 0
#         j = 0
#         while i < len(a) and j < len(b):
#             x = a[i]
#             y = b[j]

#             if x < y:
#                 i += 1
#             elif x == y:
#                 c.append(a[i])
#                 i += 1
#                 j += 1
#             else:
#                 j += 1

#         return c
