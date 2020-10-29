"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        hmap = dict()
        hmap[node] = Node(node.val)

        stack = [node]

        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in hmap:
                    stack.append(neighbor)
                    hmap[neighbor] = Node(neighbor.val)
                hmap[n].neighbors.append(hmap[neighbor])

        return hmap[node]
