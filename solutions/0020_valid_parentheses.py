# https://leetcode.com/problems/valid-parentheses/


openBrackets = ["(", "[", "{"]
closedBrackets = [")", "]", "}"]


# T: O(n)
# S: O(n)
class Solution:
    def isValid(self, brackets: str) -> bool:
        stack: list[str] = []
        for bracket in brackets:
            if bracket in openBrackets:
                stack.append(bracket)
            else:
                closedBracket = openBrackets[closedBrackets.index(bracket)]
                if len(stack) == 0 or stack.pop() != closedBracket:
                    return False
        return len(stack) == 0
