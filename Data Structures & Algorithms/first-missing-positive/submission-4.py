class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0
        res = 1

        def in_bounds(i):
            if i >= 0 and i < len(nums):
                return True
            return False

        for i, n in enumerate(nums):
            
            idx = abs(n) - 1
            if in_bounds(idx):
                num = -abs(nums[idx])
                if num == 0:
                    num = -1
                nums[idx] = num

        # if we have a length of 3 the max number our missing positive could be is len(nums) + 1
        # start at i = 1 and have res go through it and just check does that number exist super cool
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
