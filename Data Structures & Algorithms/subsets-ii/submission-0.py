class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, arr):
            if i >= len(nums):
                res.append(arr.copy()) 
                return

            # case with nums[i]
            arr.append(nums[i])
            dfs(i+1, arr)
            # case without nums[i]
            arr.pop()
            no_i = i
            while no_i < len(nums) and nums[no_i] == nums[i]:
                no_i += 1
            dfs(no_i, arr)
        dfs(0,[])
        return res