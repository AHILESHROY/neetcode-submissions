class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])

        def capture(i,j):
            if (i<0 or i>=rows or j<0 or j>=cols or board[i][j]!="O"):
                return
            board[i][j]="T"
            capture(i+1,j)    
            capture(i,j+1)    
            capture(i-1,j)    
            capture(i,j-1)
        for i in range(rows):
            capture(i,0)
            capture(i,cols-1)
        for j in range(cols):
            capture(0,j)
            capture(rows-1,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"
                                    
            