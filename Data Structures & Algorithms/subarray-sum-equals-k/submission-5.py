class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        res = 0
        c_sum = 0
        for n in nums:
            c_sum += n
            if c_sum - k in prefix:
                res += prefix[c_sum-k]
            prefix[c_sum] = prefix.get(c_sum,0) + 1
        return res