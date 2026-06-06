class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, arr, curr_sum):
            if curr_sum == target:
                res.append(arr.copy())
                return
            if curr_sum > target or i >= len(candidates):
                return

            # include the value at candidates[i]
            arr.append(candidates[i])
            dfs(i+1, arr, curr_sum + candidates[i])
            arr.pop()

            # exclude any value that is the same as candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            # we do i+1 because this will stop when we have 1 2 at 1 when we have 11112
            dfs(i + 1, arr, curr_sum)
        
        dfs(0,[],0)
        
        return res