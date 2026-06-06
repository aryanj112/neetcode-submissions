class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        cache = [2, 3]
        i = 4
        while i <= n:
            tmp = cache[1]
            cache[1] = cache[1] + cache[0]
            cache[0] = tmp
            i += 1
            
        print(cache)
        return cache[1]