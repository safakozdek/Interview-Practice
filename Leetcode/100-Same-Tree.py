# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack1 = [p]
        stack2 = [q]

        while stack1 or stack2:
            cur1 = stack1.pop()
            cur2 = stack2.pop()

            if not cur1 or not cur2:
                if cur1 == cur2:
                    continue

                return False

            if cur1.val != cur2.val:
                return

            stack1.append(cur1.left)
            stack1.append(cur1.right)
            stack2.append(cur2.left)
            stack2.append(cur2.right)

        return True
