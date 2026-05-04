class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        1) Define all the ways that you can move from your current position
        2) add starting position to a stack
        3) do a bfs from the start adding moves and there 
        """
        h,w = len(grid) - 1,len(grid[0]) - 1
        visited = set()
        def check(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x,y) not in visited and grid[x][y] == 0:
                return True
            return False
        moves = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]
        start = (1,(0,0))
        if grid[0][0] == 1:
            return -1
        visited.add((0,0))
        q = deque([start])
        while q:
            steps,position = q.popleft()
            x,y = position
            if x == h and y == w:
                return steps
            for dx,dy in moves:
                nx,ny,nsteps = x + dx, y + dy,steps + 1
                if not check(nx,ny):
                    continue
                visited.add((nx,ny))
                q.append((nsteps,(nx,ny)))
        return -1