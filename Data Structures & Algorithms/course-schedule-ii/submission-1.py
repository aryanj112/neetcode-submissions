class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topSort = []
        visit = set()
        visiting = set()
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        def dfs(i):
            if i in visiting:
                return False
            if i in visit:
                return True

            visit.add(i)
            visiting.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            # traverse all of the neighbors
            visiting.remove(i)
            topSort.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort