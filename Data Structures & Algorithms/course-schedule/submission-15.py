class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # what we can do is make a graph where each course is a node
        # and its prereqs have edges

        # prereq -> course

        adj = defaultdict(list)

        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        
        def dfs(crs, visit):
            if crs in visit:
                return False
            visit.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq, visit):
                    return False
                visit.remove(prereq)

            return True
        
        for i in range(numCourses):
            visit = set()
            if not dfs(i, visit):
                return False
        return True