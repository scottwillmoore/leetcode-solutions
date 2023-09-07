# https://leetcode.com/problems/two-sum/


# T: O(n)
# S: O(n)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        differences = {}
        for i, n in enumerate(numbers):
            if n in differences:
                return [differences[n], i]
            differences[target - n] = i
        raise
