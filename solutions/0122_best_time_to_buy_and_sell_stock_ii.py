# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


# T: O(n)
# S: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
