class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()

        for n in nums:
            hashSet.add(n)
        
        res = 0
        for n in nums:
            if n - 1 not in hashSet:
                curr = 1
                while n + curr in hashSet:
                    curr += 1
                res = max(res, curr)
        return res