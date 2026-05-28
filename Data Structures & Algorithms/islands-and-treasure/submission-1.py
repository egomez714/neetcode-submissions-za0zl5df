class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find nearest chest
        # chest = 0
        # Infinity = 2147483647
        # wall = -1

        ROWS, COLS = len(grid),len(grid[0])
        que = deque()
        visit = set()
        def addRoom(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1:
                return
            que.append((r,c))
            visit.add((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    que.append((r,c))
                    visit.add((r,c))
        distance = 0
        while que:
            # goes by levels
            for node in range(len(que)):
                curRow, curCol = que.popleft()
                grid[curRow][curCol] = distance
                addRoom(curRow + 1, curCol)
                addRoom(curRow -1, curCol)
                addRoom(curRow,curCol+1)
                addRoom(curRow,curCol-1)
            distance += 1

                