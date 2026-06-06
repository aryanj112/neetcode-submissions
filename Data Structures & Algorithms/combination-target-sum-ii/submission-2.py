class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # [9,2,2,4,6,1,5], target = 8
        # 9 and say ok one set is the set of all solutions with 9 
        # and one is the set without 9
        # takes in the current in the array, 
        res = []
        candidates.sort()
        def dfs(i, curr, arr):
            if curr == target:
                res.append(arr[:])
                return
            if curr > target or i >= len(candidates):
                return
            no_val = i
            val = candidates[i]
            while no_val < len(candidates) and candidates[no_val] == val:
                no_val += 1
            dfs(i+1, curr + val, arr + [val])    
            dfs(no_val, curr, arr)
        dfs(0, 0, [])
        return res