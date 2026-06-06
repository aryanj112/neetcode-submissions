class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)        
        
        for src, dest in tickets:
            adj[src].append(dest)
        print(adj)
        res = ['JFK']
        def dfs(src):
            print(src, adj[src],res)
            if len(res) == (len(tickets) + 1):
                print('HELLOOO')
                return True
            if src not in adj or len(adj[src]) == 0:
                return False            
            temp = adj[src].copy()
            for i, dest in enumerate(temp):
                adj[src].pop(i)
                res.append(dest)
                if dfs(dest): return True
                adj[src].insert(i,dest)
                res.pop()
            return False
        dfs('JFK')
        return res

    #     {'BUF': [], 'HOU': [], 'JFK': []}
    # len res == 4
    # res = ['JFK','BUF','HOU', 'SEA']
    # dfs(JFK) -> True
    # temp = ['BUF']
    # 0, 'BUF'

    # dfs('BUF') -> True
    # temp = ['HOU']
    # 0, 'HOU'

    # dfs('HOU') -> True
    # temp = ['SEA']
    # 0, 'SEA'

    # dfs('SEA') -> True


