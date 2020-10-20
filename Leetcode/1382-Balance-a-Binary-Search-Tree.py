# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedNodes = []

        def traverse(self, root):
            if root is None:
                return None

            traverse(self, root.left)
            self.sortedNodes.append(root)
            traverse(self, root.right)

            return None

        def constructBalanced(self, left, right):
            if left >= right:
                return None

            mid = (left + right) // 2
            root = self.sortedNodes[mid]
            root.left = constructBalanced(self, left, mid)
            root.right = constructBalanced(self, mid + 1, right)

            return root

        traverse(self, root)
        return constructBalanced(self, 0, len(self.sortedNodes))
