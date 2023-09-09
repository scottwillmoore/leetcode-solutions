# https://leetcode.com/problems/teemo-attacking/


# T: O(n)
# S: O(1)
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        totalDuration = duration
        for i in range(len(timeSeries) - 1):
            totalDuration += min(duration, timeSeries[i + 1] - timeSeries[i])
        return totalDuration
