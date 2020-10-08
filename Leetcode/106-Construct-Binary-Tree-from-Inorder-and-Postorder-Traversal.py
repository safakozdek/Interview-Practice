# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def helper(postEnd, inStart, inEnd):
            if postEnd < 0:
                return None
            if inStart > inEnd:
                return None

            root = TreeNode(postorder[postEnd])
            inIndex = inorder.index(root.val)

            root.left = helper(postEnd - (inEnd - inIndex) - 1, inStart, inIndex - 1)
            root.right = helper(postEnd - 1, inIndex + 1, inEnd)

            return root

        return helper(len(postorder) - 1, 0, len(inorder) - 1)
