class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preReq = defaultdict(set)
        visit = set()
        for prq, crs in prerequisites:
            preReq[crs].add(prq)
        inDirect = {}

        def dfs(i):
            if i in inDirect:
                return inDirect[i]
            inDirect[i] = set()
            inDirect[i] |= preReq[i]
            for nei in preReq[i]:
                inDirect[i] |= dfs(nei) | {nei}            
            return inDirect[i] | {i}
        
        for i in range(numCourses):
            dfs(i)
        res = []
        for pre, crs in queries:
            if pre in inDirect[crs]:
                res.append(True)
            else:
                res.append(False)

        return res