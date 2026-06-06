class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        postfix = [0] * len(height)

        for i in range(1,len(height)):
            prefix[i] = max(height[i-1], prefix[i-1])
        for i in range(len(height)-2,-1,-1):
            postfix[i] = max(height[i+1], postfix[i+1])
        res = 0
        for i, n in enumerate(height):
            water_trap = min(prefix[i],postfix[i]) - n
            if water_trap > 0:
                res += water_trap
        return res