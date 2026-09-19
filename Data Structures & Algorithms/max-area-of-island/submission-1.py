class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        area=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if (r<0 or c<0 or c>=cols or r>=rows or grid[r][c]==0):
                return 0
            grid[r][c]=0
            
            return (1+dfs(r+1,c)
            +dfs(r,c+1)
            +dfs(r-1,c)
            +dfs(r,c-1))
            
                



        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    grid[i][j]=0
                max_area=max(area,max_area)    
        return max_area

