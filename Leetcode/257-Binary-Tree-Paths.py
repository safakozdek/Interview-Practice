# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS - iterative
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:  # empty check
            return []
        result = []
        stack = [(root, "")]  # store tuple -> (node, path)

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:  # if leaf
                result.append(path + str(node.val))
                continue
            # Add children to stack
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))

        return result

        # BFS - iterative
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        if not root:  # empty check
            return []
        result = []
        queue = [(root, "")]  # store tuple -> (node, path)

        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:  # if leaf
                result.append(path + str(node.val))
                continue
            # Add children to stack
            if node.right:
                queue.append((node.right, path + str(node.val) + "->"))
            if node.left:
                queue.append((node.left, path + str(node.val) + "->"))

        return result


"""
1. Check empty case right away. 
- Checking it later might cause nested ifs
- A lot more readable

2. Use a stack/queue of tuple -> (node, path)
- Path is stored as string 
- Only keeping track of nodes won't work, we need paths

3. Modify paths before adding children
- path += str(node.val) + "->"

4. In leaf nodes add path to result.
result.append(path + str(node.val))
"""
