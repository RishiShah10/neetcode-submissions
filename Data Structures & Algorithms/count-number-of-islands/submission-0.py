class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """"
        go through the grid 
        1) if you find a 1 then do a dfs marking them back to 0
        2) every main dfs call add to count
        3)return count
        """
        def dfs(i,j):
            directions = [(1,0),(0,1),(0,-1),(-1,0)]
            if i >= 0 and i < len(grid) and j >=0 and j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                for x,y in directions:
                    dfs(i + x, j + y)
            else:
                return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    print("Found land")
                    dfs(i,j)
                    count += 1
        return count


        