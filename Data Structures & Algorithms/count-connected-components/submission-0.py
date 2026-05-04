class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        we can make an adj list, and from there go through 0 to n
        1) adj list
        2) iterate 0 to n
        3) if not in visited add one to connected components and dfs it
        4) return number of dfs calls
        """
        adjList = defaultdict(list)
        visited = set()
        dfsCalls = 0
        for edge in edges:
            a,b = edge
            adjList[a].append(b)
            adjList[b].append(a)
        def dfs(i):
            visited.add(i)
            for neighbor in adjList[i]:
                if neighbor not in visited:
                    dfs(neighbor)
            return
        for i in range(n):
            if i not in visited:
                dfsCalls += 1
                dfs(i)
        return dfsCalls


        