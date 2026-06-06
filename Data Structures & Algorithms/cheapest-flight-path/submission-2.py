class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * (n)
        prices[src] = 0
        adj = {src : [] for src,dest,price in flights}
        for flight in flights:
            adj[flight[0]].append([flight[1],flight[2]])
        for i in range(k + 1):
            temp_prices = prices.copy()
            for i, airport in enumerate(temp_prices):
                curr_cost = prices[i]
                if curr_cost == float('inf') or i not in adj:
                    continue
                for loc, cost in adj[i]:
                    if curr_cost + cost < temp_prices[loc]:
                        temp_prices[loc] = curr_cost + cost
            prices = temp_prices
        return -1 if prices[dst] == float('inf') else prices[dst]