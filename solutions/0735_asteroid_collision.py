# https://leetcode.com/problems/asteroid-collision/


# T: O(n)
# S: O(n)
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []

        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)

        return stack
