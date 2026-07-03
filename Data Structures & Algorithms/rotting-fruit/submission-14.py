class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Go through the grid and add all rotten fruit to a queue
        count all fresh fruit
        bfs till fresh fruit is done or none in queue
        if fresh fruit left -> -1
        else return round
        """
        q = deque()
        directions =[(0,1),(1,0),(0,-1),(-1,0)]
        r,c = len(grid),len(grid[0])
        fresh = 0
        minute = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if fresh == 0:
            return minute
        while q:
            rottenInRound = len(q)
            for i in range(rottenInRound):
                x,y = q.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        fresh -=1
                        grid[nx][ny] = 2
                        q.append((nx,ny))

                
            

            minute += 1
            if fresh == 0:
                return minute
        return -1

        