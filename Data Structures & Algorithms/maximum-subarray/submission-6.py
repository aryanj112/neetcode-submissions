class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        res = None
        for n in nums:
            if prefix < 0:
                prefix = 0
            
            prefix += n

            if not res:
                res = prefix
            else:
                res = max(res, prefix)
        return res