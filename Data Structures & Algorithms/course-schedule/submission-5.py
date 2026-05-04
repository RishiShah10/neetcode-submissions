class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        go from 0 to num courses checking if you can do each one (one for loop)
        to check if you we should make a map of each class b and its prereqs.
        starting at class 0 check its pre reqs see if theres an infintie loop so class 0 requires class 4 , class 4 requires 0 
        then return false for it
        1) make adjcanecy list 
        2) go through each course
        3) check if theres infinte loop in a dfs loop
        -- we need to remove after checking one of the pre reqs. this is because other class could be prereqs
        that are also just solo prepreqs of the main one
        visited is needed for the current recursion stakc
        4) if so break out and return false
        5) if none return true
        """
        #1
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        print(graph)

        def check(i,visited):
            print(i,visited, "loop")
            if i in visited:
                return False
            visited.add(i)
            for pre in graph[i]:
                if check(pre,visited) == False:
                    return False
            visited.remove(i)
            return True

        for i in range(numCourses):
            visited = set()
            print("USING I ", i)
            if check(i, visited) == False:
                return False

        return True


        