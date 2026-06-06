class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
     
        for n in numSet:
            # is it the start of a sequence
            if n-1 not in numSet:
                curr = 1
                i = n+1
                while i in numSet:
                    curr += 1
                    i += 1
                res = max(curr,res)

        return res