class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0
        stack = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] != "1" or (i, j) in visited:
                    continue
                count += 1
                stack.append((i, j))
                while stack:
                    cur = stack.pop()
                    visited.add((cur[0], cur[1]))
                    # check neighbours
                    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                    for side in neighbours:
                        curRow = cur[0] + side[0]
                        curCol = cur[1] + side[1]
                        validRow = row > curRow >= 0
                        validCol = col > curCol >= 0
                        visitCheck = (curRow, curCol) not in visited

                        if visitCheck and validRow and validCol and grid[curRow][curCol] == "1":
                            stack.append((curRow, curCol))

        return count
