class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        for this we are going to do a bfs where we find an island we bfs through it marking all land
        as discovered
        """
        r,c = len(grid),len(grid[0])
        island_count = 0
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def bfs(i,j):
            q = [(i,j)]
            while q:
                a,b = q.pop()
                for x,y in directions:
                    ax,by = a+x,b+y
                    if 0 <= ax < r and 0 <= by < c and grid[ax][by] == "1":
                        grid[ax][by] = "0"
                        q.append((ax,by))
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    island_count += 1
                    grid[i][j] = "0"
                    bfs(i,j)
        
        return island_count
        