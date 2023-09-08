# https://leetcode.com/problems/plus-one/


# T: O(n)
# S: O(n)
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                break
        return digits
