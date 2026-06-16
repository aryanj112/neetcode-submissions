class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}

        for idx, num in enumerate(nums):
            if (target - num) in num_to_idx:
                return [num_to_idx[(target - num)],idx]
            num_to_idx[num] = idx
