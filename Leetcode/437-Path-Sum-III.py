# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        if not root:
            return 0
        result = 0
        stack = [(root, 0)]  # stores tuples -> (node, sum)
        while stack:
            node, summation = stack.pop()
            summation += node.val

            if summation == s:
                result += 1

            if node.left:
                stack.append((node.left, summation))
            if node.right:
                stack.append((node.right, summation))

        return result