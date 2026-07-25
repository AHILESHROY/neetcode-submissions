class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            if (row<0 or col <0 or col>=len(grid[0])or row>=len(grid) or grid[row][col]=="0"):
                return 
            grid[row][col]="0"

            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        island=0
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    island+=1
                    dfs(i,j)
        return island                
                 