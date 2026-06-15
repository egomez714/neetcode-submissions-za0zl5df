class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COLS = len(grid), len(grid[0])
        res = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = "0"
            while queue:
                for i in range(len(queue)):
                    curRow, curCol = queue.popleft()
                    for updateRow,updateCol in directions:
                        newRow,newCol = updateRow + curRow, updateCol + curCol
                        if newRow >= 0 and newCol >= 0 and newCol != COLS and newRow != ROW and grid[newRow][newCol] == "1":
                            queue.append((newRow,newCol))
                            grid[newRow][newCol] = "0"
            return 1
            
        for row in range(ROW):
            for col in range(COLS):
                if grid[row][col] == "1":
                    res += bfs(row,col)
        return res