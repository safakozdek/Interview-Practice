# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(preStart, inStart, inEnd):
            if preStart >= len(preorder):
                return None
            if inStart > inEnd:
                return None

            root = TreeNode(preorder[preStart])
            inIndex = inorder.index(root.val)

            root.left = helper(preStart + 1, inStart, inIndex - 1)
            root.right = helper(preStart + 1 + inIndex - inStart, inIndex + 1, inEnd)

            return root

        return helper(0, 0, len(inorder) - 1)
