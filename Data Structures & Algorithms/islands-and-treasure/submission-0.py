class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        inf=2147483647
        directions=[(1,0),(0,1),(-1,0),(0,-1)]


        def bfs(r,c):
            q=collections.deque([(r,c)])
            visit=[[False]*cols for _ in range(rows)]
            visit[r][c]=True
            steps=0
            while q:
                for i in range(len(q)):
                    row,col=q.popleft()
                    if grid[row][col]==0:
                        return steps
                    for dr,dc in directions:
                        nr,nc=dr+row,dc+col
                        if (0 <= nr <rows and 0 <= nc < cols and
                            not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc]=True
                            q.append((nr,nc))   
                steps+=1
            return inf

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==inf:
                    grid[i][j]=bfs(i,j)    

