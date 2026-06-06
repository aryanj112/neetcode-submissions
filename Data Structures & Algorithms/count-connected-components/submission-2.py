class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}

        for i in range(n):
            par[i] = i
            rank[i] = 0

        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            return True

        res = 0
        for e1, e2 in edges:
            union(e1,e2)
        
        for i in range(n):
            if par[i] == i:
                res += 1
        return res