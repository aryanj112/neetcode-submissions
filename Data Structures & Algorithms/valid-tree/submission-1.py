class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = { i:[] for i in range(n)}
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        count = 1
        visit = set()
        def dfs(node, prev):
            nonlocal count
            if node in visit:
                return False
            
            visit.add(node)
            for neighbor in neighbors[node]:
                res = True
                if neighbor != prev:
                    res = dfs(neighbor,node)
                    count += 1
                if not res:
                    return False
            visit.remove(node)
            return True

        for i in range(n):
            count = 1
            res = dfs(i, -1)
            if count != n or not res:
                return False
        return True

