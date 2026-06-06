class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    # we start with the array of the first element and say ok 
    # I have two decisions, either 1.) add more or two add none
            # we can do taht 
        res = []
        def dfs(i, curr, arr):
            if curr == target:
                res.append(arr[:])
                return
            if i >= len(nums) or curr > target:
                return
            val = nums[i]
            dfs(i, curr + val, arr + [val])
            dfs(i + 1, curr, arr)
        dfs(0, 0, [])
        return res

        # nums=[2,5,6,9]
        # target=9
        
        # i = 0, curr = 0
        # val = 2
        # dfs(0,2,[2])
        # dfs(1,2,)


