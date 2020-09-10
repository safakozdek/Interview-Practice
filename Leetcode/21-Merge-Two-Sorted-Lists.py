# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2):
            return None
        head = mergedList = ListNode()
        while l1 and l2:
            mergedList.val = min(l1.val, l2.val)
            mergedList.next = ListNode()
            mergedList = mergedList.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next

        if l1:
            mergedList.val = l1.val
            mergedList.next = l1.next
        if l2:
            mergedList.val = l2.val
            mergedList.next = l2.next

        return head
