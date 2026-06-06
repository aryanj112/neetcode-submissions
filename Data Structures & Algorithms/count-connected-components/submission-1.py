class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i:[] for i in range(n)}
        comps = 0
        visit = set()
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def dfs(node):
            nonlocal comps
            if node in visit:
                return
            
            visit.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visit:
                    dfs(neighbor)

        for i in range(n):
            before = len(visit)
            dfs(i)
            after = len(visit)
            if after > before:
                comps += 1
        return comps