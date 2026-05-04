class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        lets build an adjc map of node and edge
        i think we then go through number edges in reverse order and see if we remove 
        from our map if we can dfs and go visit all nodes dfs style
        """
        adjMap = defaultdict(list)
        n = len(edges)
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        def dfs(node,dx,dy):
            if node in visited:
                return
            visited.add(node)
            for nx in adjMap[node]:
                if (node == dx and nx == dy) or (node == dy and nx == dx):
                    continue
                dfs(nx,dx,dy)

        for dx,dy in reversed(edges):
            visited = set()
            dfs(1,dx,dy)
            if len(visited) == (n):
                return[dx,dy]




        return [-1,-1]