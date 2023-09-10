# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


# digitToLetters = {
#     "2": ["a", "b", "c"],
#     "3": ["d", "e", "f"],
#     "4": ["g", "h", "i"],
#     "5": ["j", "k", "l"],
#     "6": ["m", "n", "o"],
#     "7": ["p", "q", "r", "s"],
#     "8": ["t", "u", "v"],
#     "9": ["w", "x", "y", "z"],
# }


def getDigit(i: int) -> str:
    return chr(ord("2") + i)


def getLetters(i: int) -> list[str]:
    return [chr(ord("a") + 3 * i + (i > 5) + j) for j in range(3)]


digitToLetters = {getDigit(i): getLetters(i) for i in range(8)}
digitToLetters["7"].append("s")
digitToLetters["9"].append("z")


# x^n + x^1 + x^2 + ... x^n = (x^n - 1) / (x - 1)
# 4^0 + 4^1 + 4^2 + ... 4^n = (4^n - 1) / 3
# O(4^0 + 4^1 + 4^2 + 4^n) = O(4^n)


# T: O(4^n)
# S: O(4^n)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combinations: list[str] = []

        i = 0
        if i < len(digits):
            digit = digits[i]
            letters = digitToLetters[digit]
            combinations.extend(letters)
            i += 1

        while i < len(digits):
            nextCombinations: list[str] = []
            for combination in combinations:
                digit = digits[i]
                letters = digitToLetters[digit]
                for letter in letters:
                    nextCombinations.append(combination + letter)
            combinations = nextCombinations
            i += 1

        return combinations
