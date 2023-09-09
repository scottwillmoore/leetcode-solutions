# https://leetcode.com/problems/merge-sorted-array/


# T: O(m + n)
# S: O(1)
class Solution:
    def merge(self, a: list[int], m: int, b: list[int], n: int) -> None:
        i = m
        while i > 0:
            i -= 1
            a[i + n] = a[i]
        j = 0
        while j < n:
            if i < m and a[i + n] < b[j]:
                a[i + j] = a[i + n]
                i += 1
            else:
                a[i + j] = b[j]
                j += 1
