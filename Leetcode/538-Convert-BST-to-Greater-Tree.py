# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.counter = 0

        def helper(self, head):
            if head is None:
                return 0

            helper(self, head.right)
            self.counter += head.val
            head.val = self.counter
            helper(self, head.left)

            return None

        helper(self, root)
        return root
