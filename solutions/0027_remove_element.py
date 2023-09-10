# https://leetcode.com/problems/remove-element/


# T: O(n)
# S: O(1)
class Solution:
    def removeElement(self, numbers: list[int], number: int) -> int:
        i = 0
        j = len(numbers)
        while i < j:
            if numbers[i] == number:
                j -= 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                i += 1
        return j
