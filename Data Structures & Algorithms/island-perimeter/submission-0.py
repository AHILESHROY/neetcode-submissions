class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        row=len(grid)
        col=len(grid[0])
        visited=set()
        def bfs(r,c):
            queue=deque([(r,c)])
            visited.add((r,c))
            perimeter=0
            while queue:
                x,y=queue.popleft()
                for a,b in directions:
                    nx,ny=x+a,y+b
                    if (nx<0 or nx>=row or ny<0 or ny>=col or grid[nx][ny]==0):
                        perimeter+=1
                    elif (nx,ny) not in visited:
                        visited.add((nx,ny)) 
                        queue.append((nx,ny))   
            return perimeter
        for i in range(row):
            for j in range(col):
                if grid[i][j] ==1:
                    return bfs(i,j)
        return 0




