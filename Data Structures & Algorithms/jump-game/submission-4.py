class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0      # index of the current number we are at
        prefix = 0 # number of spaces we can jump forward 
                    # off of our current location using previous values

        while i < len(nums) - 1: # once the index is the last element or more we are good
            if prefix < 1 and nums[i] == 0:
                return False
            elif nums[i] > prefix:
                prefix = nums[i] - 1
            else:
                prefix -= 1
            i += 1

        return True