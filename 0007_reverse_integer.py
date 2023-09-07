# https://leetcode.com/problems/reverse-integer/


# T: O(n)
# S: O(n)
# NOTE: `n` is the number of digits in `x`.
class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0

        if isNegative:
            x = -x

        reversed_digits: list[int] = []
        while x > 0:
            reversed_digits.append(x % 10)
            x //= 10

        reversed_number = 0
        for i, d in enumerate(reversed_digits):
            p = len(reversed_digits) - i - 1
            reversed_number += 10**p * d

        if isNegative:
            reversed_number = -reversed_number

        if not (-(2**31) <= reversed_number <= 2**31 - 1):
            return 0

        return reversed_number
