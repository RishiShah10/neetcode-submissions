class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        a group of courses is not finishable if theres is a cycle
        1) create the adjacenyList
        2) go through from course 0 to num courses
        3) check if theres a cycle with it
        4) if so return false
        """
        adjList = defaultdict(list)
        for a,b in prerequisites:
            adjList[a].append(b)
        def dfs(i,visited):
            if i in visited:
                return False
            visited.add(i)
            for pre in adjList[i]:
                if dfs(pre,visited) == False:
                    return False
                visited.remove(pre)
            return True
        for i in range(numCourses):
            visited = set()
            if dfs(i,visited) == False:
                return False
        return True