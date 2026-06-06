class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        descendents = defaultdict(set)
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs not in descendents:
                for neighbor in adj[crs]:
                    descendents[crs] |= dfs(neighbor)
                descendents[crs].add(crs)
            return descendents[crs]

        for i in range(numCourses):
            dfs(i)
        
        res = []
        for pre, crs in queries:
            res.append(pre in descendents[crs])
        return res