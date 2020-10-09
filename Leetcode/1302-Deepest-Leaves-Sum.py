# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        result = 0
        max_d = -1
        stack = [(root, 0)]

        while stack:
            current = stack.pop()
            if current[1] > max_d:
                max_d = current[1]

            if current[0].left:
                stack.append((current[0].left, current[1] + 1))

            if current[0].right:
                stack.append((current[0].right, current[1] + 1))

        stack2 = [(root, 0)]
        while stack2:
            current = stack2.pop()
            if current[1] == max_d:
                result += current[0].val
            if current[0].left:
                stack2.append((current[0].left, current[1] + 1))

            if current[0].right:
                stack2.append((current[0].right, current[1] + 1))

        return result
