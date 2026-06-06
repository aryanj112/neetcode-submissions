class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        print(adj)

        indirect_prereqs = defaultdict(set)
        visit = set()

        def dfs(crs):
            # if not adj[crs]:
            #     return {crs}
            if crs in indirect_prereqs:
                return indirect_prereqs[crs] | {crs}
            for nei in adj[crs]:
                indirect_prereqs[crs] |= dfs(nei) | {nei}
            return indirect_prereqs[crs] | {crs}
        
        for i in range(numCourses):
            dfs(i)

        res = []
        for pre, crs in queries:
            if pre in indirect_prereqs[crs]:
                res.append(True)
            else:
                res.append(False)
        return res
