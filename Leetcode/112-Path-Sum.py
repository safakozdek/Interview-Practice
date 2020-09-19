# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return False

        stack = [(root, 0)]  # stack stores -> (node, sum)

        # iterative dfs
        while stack:
            node, summation = stack.pop()
            new_sum = summation + node.val
            if not node.left and not node.right:  # if leaf
                if new_sum == s:
                    return True
            if node.left:
                stack.append((node.left, new_sum))
            if node.right:
                stack.append((node.right, new_sum))

        return False
