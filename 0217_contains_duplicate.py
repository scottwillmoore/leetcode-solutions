# https://leetcode.com/problems/contains-duplicate/


# T: O(n)
# S: O(n)
class Solution:
    def containsDuplicate(self, numbers: list[int]) -> bool:
        numbersSet = set[int]()
        for number in numbers:
            if number in numbersSet:
                return True
            else:
                numbersSet.add(number)
        return False
