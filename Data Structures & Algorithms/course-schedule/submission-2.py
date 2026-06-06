class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = { i:[] for i in range(numCourses) }
        for c, p in prerequisites:
            preMap[c].append(p)
        
        print(preMap)
        
        def dfs(course):
            if course in visit:
                return False
            if not preMap[course]:
                return True
            visit.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        #{0: [1], 1: [0]}



