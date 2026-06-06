class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m

            if nums[m] >= nums[l]: 
                # we are in the left 
                if target < nums[m] and target >= nums[l]:
                    # the target is in the left sorted array
                    r = m - 1
                else:
                    # this is saying we are in the left and the target is not so lets go to the right
                    l = m + 1
            else:
                # we are in the right
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1


        return -1