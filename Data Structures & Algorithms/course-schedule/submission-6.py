class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adj list that maps a crs to a list of its direct prereqs
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        print(adj)

        # traverse from any given node through all of its paths and if it sees
        # a cycle return False
        def dfs(i):
            # if we have already seen this node then we know it has been visited
            # again via a cycle
            if i in visit:
                return False
            # if adj[i] == [] we know this course is valid, we are able to take it
            if not adj[i]:
                is_valid[i] = True
                return True

            visit.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            is_valid[i] = True
            return True
            
        # we are doing a dfs on every node because we dont know where the root
        # node in this directed acyclic graph is (or is it a DAG)
        # is valid crs
        is_valid = {}
        for i in range(numCourses):
            visit = set()
            if i in is_valid:
                continue
            if not dfs(i):
                return False    
            is_valid[i] = True
        return True