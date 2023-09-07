# https://leetcode.com/problems/valid-palindrome/


# T: O(n)
# S: O(n)
class Solution:
    def isPalindrome(self, phrase: str) -> bool:
        filtered_phrase = list(filter(str.isalnum, phrase.lower()))
        reversed_phrase = list(reversed(filtered_phrase))
        return filtered_phrase == reversed_phrase
