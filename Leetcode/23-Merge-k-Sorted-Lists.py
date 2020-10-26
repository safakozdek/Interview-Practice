# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = node = ListNode(0)
        h = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(h)
        while h:
            val, i, ptr = h[0]
            if ptr.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (ptr.next.val, i, ptr.next))
            node.next = ptr
            node = node.next

        return dummy.next
