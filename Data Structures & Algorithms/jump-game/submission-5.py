class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i, prefix = 0, 0

        while i < len(nums) - 1:
            if prefix < 1 and nums[i] == 0:
                return False
            elif nums[i] > prefix:
                prefix = nums[i] - 1
            else:
                prefix -= 1
            i += 1

        return True