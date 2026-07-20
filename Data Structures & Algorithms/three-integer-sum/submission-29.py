class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for plant in range(len(nums) - 2):
            l = plant + 1
            r = len(nums) - 1
            while l < r:
                curr = nums[plant] + nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.add((nums[plant],nums[l],nums[r]))
                    l += 1
                    r -= 1
        print(res)
        new_res = []
        for value in res:
            temp = []
            for num in value:
                temp.append(num)
            new_res.append(temp.copy())
        return new_res