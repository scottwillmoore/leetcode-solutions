# https://leetcode.com/problems/permutations/


def dfs(path: list[int], children: list[int], permutations: list[list[int]]) -> None:
    if not children:
        permutations.append(path)

    for i, child in enumerate(children):
        dfs(path + [child], children[:i] + children[i + 1 :], permutations)


# T: O(n*n!)
# S: O(n!)
class Solution:
    def permute(self, numbers: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        dfs([], numbers, permutations)
        return permutations
