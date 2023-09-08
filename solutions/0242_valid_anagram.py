# https://leetcode.com/problems/valid-anagram/


from collections import Counter


# T: O(n)
# S: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# T: O(n log n)
# S: O(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
