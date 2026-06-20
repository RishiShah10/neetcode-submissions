class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        For this we need to add each bannana thats rotten to a queue, count all bannanas
        and if the bannana is rotten we go in rounds to neighbors
        once no neighbors and rounds left if all banaas have gotten rotten we return -1
        """
        q = deque()
        freshFruitCount = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        r,c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    #fresh fruit
                    freshFruitCount += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        print(q)
        if freshFruitCount == 0:
            return 0
        minute = -1
        while q:
            currentQSize = len(q)
            for i in range(currentQSize):
                x,y = q.popleft()
                print(x,y)
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        freshFruitCount -= 1
                        grid[nx][ny] = 2
                        q.append((nx,ny))
                        
            minute += 1
        if freshFruitCount > 0:
            return -1
        return minute
                


        
        