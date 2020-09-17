# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next
 """
Notes:
1. Use given Nodes, do not create new ones.

2. To create a special linked list using existing nodes:
Use two pointers to an empty node:
1 for iteration & adding new nodes
2 for returning the head of the linked list (return head.next)

3. Worst case complexity is O(n+m), best case is O(min(n,m)):
After one of the lists ends use curr.next = l1 or l2 (eliminates None)

4. If there is a priority for one of the lists for equal values, 
Fix line 10 with respect to it.
 """