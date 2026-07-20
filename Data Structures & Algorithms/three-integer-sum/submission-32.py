class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        res = []
        for plant in range(len(nums) - 2):
            l = plant + 1
            r = len(nums) - 1
            if plant != 0 and nums[plant] == nums[plant - 1]:
                continue
            while l < r:
                curr = nums[plant] + nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([nums[plant],nums[l],nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
        return res