class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
       
        islands = 0
        ROWS,COLS = len(grid),len(grid[0])
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            
            while q:
                r,c = q.popleft()
                for dl,dr in directions:
                    nr, nc = dl + r, dr + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands