class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        go through the borders
        left and the top = pacific
        right and bottom = atlantic
        bfs cells where water can flow adding them to a set
        do set union return the set union = pacific AND atlantic
        """
        p = set()
        a = set()
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        def bfs(start,flowSet):
            x,y = start
            flowSet.add((x,y))
            q = deque([start])
            while q:
                x,y = q.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and heights[nx][ny] >= heights[x][y] and (nx,ny) not in flowSet:
                        flowSet.add((nx,ny))
                        q.append((nx,ny)) 
            return

            
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    # this is pacfic starting
                    # bfs add to set
                    bfs((i,j),p)
                if i == ( len(heights) - 1) or j == (len(heights[0]) - 1):
                    # this is atlantic starting
                    #bfs add to set
                    bfs((i,j),a)
        setIntersection = p.intersection(a)
        print("Pacific:", p)
        print("Atlantic:", a)
        print("Intersection:", p.intersection(a))
        result = [list(cell) for cell in setIntersection]
        return result
        