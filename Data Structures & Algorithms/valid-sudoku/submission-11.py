class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        threeByThree = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if ( board[i][j] in row[i]
                     or board[i][j] in column[j] 
                     or board[i][j] in threeByThree[(i // 3, j //3)]):
                    return False

                column[j].add(board[i][j])
                row[i].add(board[i][j])
                threeByThree[(i//3,j//3)].add(board[i][j])
        return True

