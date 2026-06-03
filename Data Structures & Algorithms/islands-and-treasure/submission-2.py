class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # -1 a wall
        # 0 treasure chest
        # INF = land cell
        INF = 2147483647
        ROWS,COLS = len(grid), len(grid[0])

        visited = set()
        que = deque()

        def newRoom(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            que.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    que.append([r,c])
        distance = 0
        while que:
            for i in range(len(que)):
                newR, newC = que.popleft()
                grid[newR][newC] = distance
                newRoom(newR + 1,newC)
                newRoom(newR - 1,newC)
                newRoom(newR,newC + 1)
                newRoom(newR,newC - 1)
            distance += 1
