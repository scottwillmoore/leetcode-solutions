# https://leetcode.com/problems/trapping-rain-water/


def trapForward(heights: list[int]) -> tuple[int, int]:
    i = 0
    maxHeight = 0
    totalUnits = 0
    units = 0
    for j, height in enumerate(heights):
        if maxHeight <= height:
            i = j
            maxHeight = height
            totalUnits += units
            units = 0
        else:
            units += maxHeight - height
    return totalUnits, i


# T: O(n)
# S: O(1)
class Solution:
    def trap(self, heights: list[int]) -> int:
        forwardUnits, i = trapForward(heights)
        backwardHeights = list(reversed(heights[i:]))
        backwardUnits, _ = trapForward(backwardHeights)
        return forwardUnits + backwardUnits
