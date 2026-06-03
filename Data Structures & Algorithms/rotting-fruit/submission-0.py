class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find infected first two loops 
        # add to que and use bfs to go off levels
        # keep counter after every loop
        # use helper to update grid
        # if all fruit = 2 return counter else return -1

        ROWS,COLS = len(grid),len(grid[0])

        que = deque()
        bananas = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    que.append((r,c))
                elif grid[r][c] == 1:
                    bananas += 1
        minutes = 0
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        while que and bananas > 0:  # added banana count  
            for i in range(len(que)):
                newR,newC = que.popleft()
                # added directions 
                for dr,dc in directions:
                    row,col = dr + newR, dc + newC
                    if (row < 0 or row == ROWS or
                     col < 0 or col == COLS or 
                     grid[row][col] != 1):
                     continue

                    grid[row][col] = 2
                    que.append((row,col))
                    bananas -=1
            minutes += 1
        return minutes if bananas == 0 else -1