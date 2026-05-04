class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        1) check if theres a cycle from any node
        2) do a bfs with nodes that dont have any prerequisites
        3) then lets see which ones thoughs courses are prereqs are for remove them from the set
        4) return result
        1) we need mappings of course to its prereqs
        2) prereqs to course you could take so prereqs and maybe set of courses it could go to
        3) a queue
        """
        courseToPre = defaultdict(set)
        preToCourse = defaultdict(set)
        result = []
        q = []
        for a,b in prerequisites:
            courseToPre[a].add(b)
            preToCourse[b].add(a)

        def dfs(i, visiting):
            if i in visiting:
                return False  # cycle
            
            visiting.add(i)
            
            for pre in courseToPre.get(i, []):
                if dfs(pre, visiting) == False:
                    return False
            
            visiting.remove(i)  # <-- FIXED
            return True
        
        for i in range(numCourses):
            if dfs(i, set()) == False:
                return []
            if i not in courseToPre or len(courseToPre[i]) == 0:
                q.append(i)
        while q:
            val = q.pop()
            print(val)
            result.append(val)
            for nextClass in preToCourse[val]:
                courseToPre[nextClass].remove(val)
                if len(courseToPre[nextClass]) == 0:
                    q.append(nextClass)
        if len(result) != numCourses:
            print("reached" , result)
            return []
        
        return result


        
