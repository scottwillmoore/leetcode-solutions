# https://leetcode.com/problems/longest-common-prefix/


# T: O(m*n)
# S: O(m)
class Solution:
    def longestCommonPrefix(self, strings: list[str]) -> str:
        head, tail = strings[0], strings[1:]
        for i, character in enumerate(head):
            for string in tail:
                if not (i < len(string) and character == string[i]):
                    return head[:i]
        return head
