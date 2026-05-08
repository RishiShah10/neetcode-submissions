class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        lets do a bfs from every time we see a point
        when we see a point we start a bfs call and then change the grid 1s to 0s
        return number of bfs calls
        """
        r,c= len(grid),len(grid[0])
        count = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(i,j):
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                grid[x][y] = "0"
                for dx,dy in directions:
                    nx,ny = x + dx,y + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                        q.append((nx,ny))     
            return
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count += 1
        return count