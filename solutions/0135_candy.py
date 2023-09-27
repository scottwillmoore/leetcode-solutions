# https://leetcode.com/problems/candy/


# T: O(n)
# S: O(n)
class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                candies[i + 1] = candies[i] + 1

        for i in reversed(range(len(ratings) - 1)):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
