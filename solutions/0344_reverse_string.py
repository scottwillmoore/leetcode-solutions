# https://leetcode.com/problems/reverse-string/


# T: O(n)
# S: O(1)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            j = len(s) - i - 1
            s[i], s[j] = s[j], s[i]
