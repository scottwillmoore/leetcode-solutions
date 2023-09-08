# https://leetcode.com/problems/move-zeroes/


# T: O(n)
# S: O(1)
class Solution:
    def moveZeroes(self, numbers: list[int]) -> None:
        i = 0
        for j in range(len(numbers)):
            if numbers[j] != 0:
                numbers[i] = numbers[j]
                i += 1

        for j in range(i, len(numbers)):
            numbers[j] = 0
