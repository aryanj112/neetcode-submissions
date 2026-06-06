class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = nums[0]

        for n in nums[1:]:
            if curr < 0:
                curr = 0
            curr += n

            res = max(res,curr)
        return res