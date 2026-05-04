class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        get all locations of rotten oranges
        add them to a stack
        go through stack after checking count for every round of bfs add to count
        return final round
        
        """
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        stack = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        minute = 0
        while stack and fresh != 0:
            for i in range(len(stack)):
                x,y = stack.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        stack.append((nx,ny))
                        fresh -= 1
            minute += 1
        if fresh != 0:
            return -1

        return minute