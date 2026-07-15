class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for n in nums:
            if n-1 not in hashset: # we have the start of a sequence
                temp = 1
                while n + 1 in hashset:
                    temp += 1
                    n += 1
                res = max(res,temp)
        return res