# https://leetcode.com/problems/can-place-flowers/


# T: O(n)
# S: O(1)
class Solution:
    def canPlaceFlowers(self, flowers: list[int], flowerCount: int) -> bool:
        maxFlowerCount = 0
        zeroCount = 0

        for flower in (0, *flowers, 0):
            if flower == 0:
                if zeroCount == 2:
                    maxFlowerCount += 1
                    if flowerCount == maxFlowerCount:
                        return True
                    zeroCount = 0
                zeroCount += 1
            else:
                zeroCount = 0

        return flowerCount <= maxFlowerCount


# T: O(n)
# S: O(1)
# class Solution:
#     def canPlaceFlowers(self, flowers: list[int], flowerCount: int) -> bool:
#         maxFlowerCount = 0
#         zeroCount = 1

#         for flower in flowers:
#             if flower == 0:
#                 if zeroCount == 2:
#                     maxFlowerCount += 1
#                     if flowerCount == maxFlowerCount:
#                         return True
#                     zeroCount = 0
#                 zeroCount += 1
#             else:
#                 zeroCount = 0

#         if zeroCount == 2:
#             maxFlowerCount += 1

#         return flowerCount <= maxFlowerCount
