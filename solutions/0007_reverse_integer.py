# https://leetcode.com/problems/reverse-integer/


# T: O(n)
# S: O(n)
class Solution:
    def reverse(self, number: int) -> int:
        isNegative = number < 0

        if isNegative:
            number = -number

        reversedDigits: list[int] = []
        while number > 0:
            reversedDigits.append(number % 10)
            number //= 10

        reversedNumber = 0
        for i, d in enumerate(reversedDigits):
            p = len(reversedDigits) - i - 1
            reversedNumber += 10**p * d

        if isNegative:
            reversedNumber = -reversedNumber

        if not (-(2**31) <= reversedNumber < 2**31):
            return 0

        return reversedNumber
