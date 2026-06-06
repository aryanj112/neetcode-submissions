class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visit = set()

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        def dfs(i):
            if i in visit:
                return 0
            visit.add(i)
            maxDepth = 0
            for nei in adj[i]:
                maxDepth = max(dfs(nei),maxDepth)
            return maxDepth + 1

        res = []
        currMin = float('inf')
        for i in range(n):
            visit = set()
            print("node", i)
            height = dfs(i)
            if height < currMin:
                res = [i]
                currMin = height
            else:
                if currMin == height:
                    res.append(i)
            print("height", height)
        return res
