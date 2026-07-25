class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            if (row<0 or col<0 or col>=len(grid[0]) or row>=len(grid) or grid[row][col]==0):
                return 0
            grid[row][col]=0
            return(1+dfs(row+1,col)
            +dfs(row,col+1)
            +dfs(row-1,col)
            +dfs(row,col-1))
        rows=len(grid)
        cols=len(grid[0])
        max_area=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    max_area=max(max_area,dfs(i,j))
        return max_area                            