class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = { i:i for i in range(n)}
        rank = { i:0 for i in range(n)}

        def find(city):
            p = par[city]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(city1, city2):
            p1, p2 = find(city1), find(city2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True

        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 0:
                    continue
                union(r,c)

        res = 0
        for city, parent in par.items():
            if city == parent:
                res += 1
        return res