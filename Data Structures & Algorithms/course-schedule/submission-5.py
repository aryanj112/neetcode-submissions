class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        adj = defaultdict(list)
        # map a crs to its prerequisites
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        print(adj)
        def dfs(i):
            print(i, visit)
            if not adj[i]:
                return True
            if i in visit:
                return False
            
            # base case that the node isnt visited and it is a valid crs bc it has
            # no prereqs
            visit.add(i)
            print(adj[i])
            for nei in adj[i]:
                print("I am doing a dfs on ", nei)
                result = dfs(nei)
                print(result)
                if not result:
                    return False
            return True

        for i in range(numCourses):
            visit = set()
            print("new iteration", i)
            if not dfs(i):
                return False
        return True
