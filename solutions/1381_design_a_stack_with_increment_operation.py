# https://leetcode.com/problems/design-a-stack-with-increment-operation/


from dataclasses import dataclass


@dataclass
class CustomElement:
    value: int
    increment: int


# S: O(n)
class CustomStack:
    maxSize: int
    stack: list[CustomElement]

    # T: O(1)
    def __init__(self, maxSize: int) -> None:
        self.maxSize = maxSize
        self.stack = []

    # T: O(1)
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(CustomElement(x, 0))

    # T: O(1)
    def pop(self) -> int:
        if not self.stack:
            return -1

        element = self.stack.pop()
        if self.stack:
            self.stack[-1].increment += element.increment

        return element.value + element.increment

    # T: O(1)
    def increment(self, k: int, increment: int) -> None:
        if self.stack:
            i = min(k, len(self.stack)) - 1
            self.stack[i].increment += increment
