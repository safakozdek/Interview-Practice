# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return [[]]

        result = []
        stack = [(root, [])]  # stack stores -> (node, [path])

        # iterative dfs
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:  # if leaf
                if sum(path) + node.val == s:
                    result.append(path + [node.val])
            if node.left:
                stack.append((node.left, path + [node.val]))
            if node.right:
                stack.append((node.right, path + [node.val]))

        return result