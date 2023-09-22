# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


# T: O(n)
# S: O(1)
class Solution:
    def removeDuplicates(self, numbers: list[int]) -> int:
        i = 0
        n = len(numbers)
        for j in range(n):
            numbers[j - i] = numbers[j]
            if j < n - 2 and numbers[j] == numbers[j + 1] == numbers[j + 2]:
                i += 1
        return n - i
