# https://leetcode.com/problems/contains-duplicate/


# T: O(N)
# S: O(N)
class Solution:
    def containsDuplicate(self, numbers_list: list[int]) -> bool:
        numbers_set = set[int]()
        for number in numbers_list:
            if number in numbers_set:
                return True
            else:
                numbers_set.add(number)
        return False
