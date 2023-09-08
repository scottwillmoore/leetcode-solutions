# https://leetcode.com/problems/merge-intervals/


# T: O(n log n)
# T: O(n)
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        mergedIntervals = sortedIntervals[:1]

        previousInterval = sortedIntervals[0]
        for interval in sortedIntervals[1:]:
            if previousInterval[1] < interval[0]:
                mergedIntervals.append(interval)
                previousInterval = interval
            else:
                previousInterval[1] = max(previousInterval[1], interval[1])

        return mergedIntervals
