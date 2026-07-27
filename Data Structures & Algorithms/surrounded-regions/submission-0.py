class Solution:
    def solve(self, board: List[List[str]]) -> None:
        cols=len(board[0])
        rows=len(board)
        
        
        def dfs(row,col):
            if(row<0 or col<0 or col==cols or row==rows or board[row][col]!="O"):
                return
            
            
            board[row][col]="T"   
                
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)    
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows- 1][c] == "O":
                dfs(rows-1,c)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="T":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"        
                  