class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        go through grid
        when see island add to visited adn return 1 + dfs directions
        """

        visited = set()
        bic = 0
        def dfs(i,j):
            if (i,j) not in visited and 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                visited.add((i,j))
                return 1 + dfs(i + 1,j) + dfs(i - 1,j) + dfs(i,j + 1) + dfs(i,j - 1)
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bic = max(bic,dfs(i,j))
        return bic

        