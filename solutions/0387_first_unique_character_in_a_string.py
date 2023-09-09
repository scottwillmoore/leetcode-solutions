# https://leetcode.com/problems/first-unique-character-in-a-string/


from collections import Counter


# T: O(n)
# S: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
