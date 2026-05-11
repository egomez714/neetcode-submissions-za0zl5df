class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,-1],[0,1],[0,0]]
        area = 0
        ROWS, COLS = len(grid),len(grid[0])
        def bfs(r,c):
            que = deque()
            que.append((r,c))
            islandSize = 0
            while que:
                row,col = que.popleft()
                for dr,dc in directions:
                    newRow, newCol = row+dr, col+dc
                    if newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLS or grid[newRow][newCol] == 0:
                        continue
                    que.append((newRow,newCol))
                    islandSize+=1
                    grid[newRow][newCol] = 0
            return islandSize
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area,bfs(r,c))
        return area

