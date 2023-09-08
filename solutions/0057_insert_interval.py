# https://leetcode.com/problems/insert-interval/


# T: O(n)
# S: O(n)
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        newIntervals: list[list[int]] = []

        i = 0
        while i < len(intervals):
            interval = intervals[i]

            if interval[1] < newInterval[0]:
                newIntervals.append(interval)
            elif newInterval[1] < interval[0]:
                break
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

            i += 1

        newIntervals.append(newInterval)
        newIntervals.extend(intervals[i:])

        return newIntervals
