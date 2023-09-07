# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


# T: O(n)
# S: O(n)
class Solution:
    def removeDuplicates(self, numbers: list[int]) -> int:
        i = 0
        for j in range(1, len(numbers)):
            if numbers[i] != numbers[j]:
                i = i + 1
                numbers[i] = numbers[j]
        return i + 1
