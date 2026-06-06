class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        print(s)
        output = 0

        for n in nums:
            curr = 0
            if n - 1 not in s:
                # this is the start of a sequence
                i = n
                while i in s:
                    curr += 1
                    i += 1
                if curr > output:
                    output = curr

        return output 