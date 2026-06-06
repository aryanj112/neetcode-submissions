class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we want to keep it all in place and all in nums
        # and then we basically want to return a number in our new nums such that
        # [1, 2, 3, 3, 4] val = 3 -> [1, 2, 4, _, _] and return 3
        
        #                    |
        # [1, 2, 4, 5, 7, 8, 3, 3, 3]
        #                           

        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k