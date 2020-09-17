# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maximum = 0

        def getHeight(node):
            if node is None:
                return 0

            left = getHeight(node.left)
            right = getHeight(node.right)
            maxForThisNode = left + right

            self.maximum = max(self.maximum, maxForThisNode)
            return 1 + max(left, right)

        getHeight(root)
        return self.maximum
