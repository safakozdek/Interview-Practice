class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        0 - cur:0 next:0
        1 - cur:1 next:0
        2 - cur:0 next:1
        3 - cur:1 next:1
        Constant Memory solution
        """

        def getSum(line, col):
            res = 0
            nears = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
            for near in nears:
                validLine = 0 <= line + near[0] < len(board)
                validCol = 0 <= col + near[1] < len(board[0])
                if validLine and validCol and board[line + near[0]][col + near[1]] % 2 == 1:
                    res += 1

            return res

        for line in range(0, len(board)):
            for col in range(0, len(board[line])):
                cur = board[line][col]
                adjSum = getSum(line, col)

                if adjSum < 2 or adjSum > 3:
                    pass
                elif cur == 1:
                    board[line][col] = 3
                elif adjSum == 3:
                    board[line][col] = 2

        # reorganize
        for line in range(0, len(board)):
            for col in range(0, len(board[line])):
                board[line][col] = board[line][col] // 2

        return board
