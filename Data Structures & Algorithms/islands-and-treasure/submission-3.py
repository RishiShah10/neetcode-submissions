class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        add every treasure chest to a stack, all 0
        then bfs from each 0 if its inf then replace it with the level of bfs we on 
        return once bfs done only add to bfs when spots are inf
        """
        queue = deque()
        inf = 2147483647
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while len(queue) != 0:
            currentLength = len(queue)
            for i in range(currentLength):
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == inf:
                        grid[nx][ny] = grid[x][y] + 1
                        queue.append((nx,ny))



