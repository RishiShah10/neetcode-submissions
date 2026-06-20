class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        For this question I want to figure out how to go through the graph
        lets go through the graph if we hit a 1 find neighbros change to 0 keep a counter
        """
        r,c = len(grid), len(grid[0])
        islandCount = 0 
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(i,j):
            if 0 <= i < r and 0 <= j < c and grid[i][j] == "1":
                grid[i][j] = "0"
                for x,y in directions:
                    dfs(i + x, j + y)
            return

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islandCount += 1
        return islandCount