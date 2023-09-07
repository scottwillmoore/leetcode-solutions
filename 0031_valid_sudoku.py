# https://leetcode.com/problems/valid-sudoku/


# T: O(1)
# S: O(1)
class Solution:
    def isValidSudoku(self, grid: list[list[str]]) -> bool:
        constraints = set[str]()

        for y in range(9):
            for x in range(9):
                cell = grid[y][x]

                if cell == ".":
                    continue

                row = f"r{x}{cell}"
                column = f"c{y}{cell}"
                box = f"b{x // 3}{y // 3}{cell}"

                for constraint in [row, column, box]:
                    if constraint in constraints:
                        return False
                    else:
                        constraints.add(constraint)

        return True
