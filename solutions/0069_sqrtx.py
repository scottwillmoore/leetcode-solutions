# https://leetcode.com/problems/sqrtx/


# T: O(log n)
# S: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        a = 0
        c = x
        while a <= c:
            b = (a + c) // 2
            b2 = b * b
            if b2 < x:
                a = b + 1
            elif b2 == x:
                return b
            else:
                c = b - 1
        return c


# T: O(n)
# S: O(1)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         i = 0
#         while i * i <= x:
#             i += 1
#         return i - 1
