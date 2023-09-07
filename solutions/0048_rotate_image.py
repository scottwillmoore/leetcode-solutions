# https://leetcode.com/problems/rotate-image/


# T: O(n*2)
# S: O(1)
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for y1 in range(n // 2):
            y2 = n - y1 - 1
            for x1 in range(y1, y2):
                x2 = n - x1 - 1

                element = matrix[x2][y1]
                matrix[x2][y1] = matrix[y2][x2]
                matrix[y2][x2] = matrix[x1][y2]
                matrix[x1][y2] = matrix[y1][x1]
                matrix[y1][x1] = element
