class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for p1, p2 in trust:
            in_degree[p2] += 1
            out_degree[p1] += 1
        for i in range(1,n+1):
            if in_degree[i] == n-1 and out_degree[i] == 0:
                return i
        return -1