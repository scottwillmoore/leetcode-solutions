# https://leetcode.com/problems/valid-palindrome/


# T: O(n)
# S: O(n)
class Solution:
    def isPalindrome(self, phrase: str) -> bool:
        filteredPhrase = list(filter(str.isalnum, phrase.lower()))
        reversedPhrase = list(reversed(filteredPhrase))
        return filteredPhrase == reversedPhrase
