class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        we make a graph of course -> courses you need to take
        for each course a course needs to take and track its depdency graph in a visited set
        if theres no loops means its possible to take the courses needed for that one
        go through a courses pre reqs and thier prereqs
        if theres every a ciruclar depdency means not possible
        so return false
        """
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        def check(i,visited):
            if i in visited:
                return False
            visited.add(i)
            for pre in graph[i]:
                if check(pre,visited) == False:
                    return False
                visited.remove(pre)
            return True
        for i in range(numCourses):
            visited = set()
            if check(i,visited) == False:
                return False
        return True