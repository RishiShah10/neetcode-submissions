class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        go through the grid, when u hit a one dfs through it markign the connected as 0
        return # base dfs calls
        """
        count = 0
        r,c = len(grid),len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            grid[i][j] = "0"
            for dx,dy in directions:
                nx,ny = i + dx,j + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                    dfs(nx,ny)
            return

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count