# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


from __future__ import annotations


class ListNode:
    val: int
    next: ListNode | None


# T: O(n)
# S: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode | None:
        z = head
        for _ in range(n):
            assert z
            z = z.next

        x = None
        y = head
        while z:
            x = y
            assert y.next
            y = y.next
            z = z.next

        if not x:
            return y.next

        x.next = y.next
        return head
