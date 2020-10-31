class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # longest path
        neighbours = defaultdict(set)
        for n1, n2 in edges:
            neighbours[n1].add(n2)
            neighbours[n2].add(n1)

        stack = [[0]]
        maxPath = []

        while stack:
            cur = stack.pop()
            if len(maxPath) < len(cur):  # update longest path
                maxPath = cur

            for neigh in neighbours[cur[-1]]:
                if len(cur) >= 2 and cur[-2] == neigh:  # avoiding loop
                    continue

                stack.append(cur + [neigh])

        stack = [[maxPath[-1]]]
        maxPath = []

        while stack:
            cur = stack.pop()
            if len(maxPath) < len(cur):
                maxPath = cur

            for neigh in neighbours[cur[-1]]:
                if len(cur) >= 2 and cur[-2] == neigh:
                    continue

                stack.append(cur + [neigh])

        l = len(maxPath)

        return maxPath[(l - 1) // 2:(l // 2 + 1)]
