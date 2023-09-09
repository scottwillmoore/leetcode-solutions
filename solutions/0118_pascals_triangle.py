# https://leetcode.com/problems/pascals-triangle/


# T: O(n^2)
# S: O(n^2)
class Solution:
    def generate(self, rowCount: int) -> list[list[int]]:
        previousRow = [1]
        rows = [previousRow]
        for i in range(1, rowCount):
            row = [1]
            for j in range(0, i - 1):
                row.append(previousRow[j] + previousRow[j + 1])
            row.append(1)
            previousRow = row
            rows.append(row)
        return rows
