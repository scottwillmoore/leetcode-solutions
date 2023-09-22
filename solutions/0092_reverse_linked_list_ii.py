# https://leetcode.com/problems/reverse-linked-list-ii/


from __future__ import annotations


class ListNode:
    val: int
    next: ListNode | None


# T: O(n)
# S: O(1)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode | None:
        a: ListNode | None = None
        b = head
        for _ in range(1, left):
            a = b
            assert b.next is not None
            b = b.next

        x = b
        y = x.next
        for _ in range(left, right):
            assert y is not None
            z = y.next
            y.next = x
            x = y
            y = z

        b.next = y

        if not a:
            return x

        a.next = x
        return head
