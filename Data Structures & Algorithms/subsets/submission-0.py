class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # we want to define a recursive helper that can go through and traverse
        # the decision tree until the output has been reached
                
        def backtrack(i, lst):
            if i == len(nums):
                res.append(lst[:])
                return
            
            lst.append(nums[i])
            backtrack(i + 1, lst)
            lst.pop()

            backtrack(i + 1, lst)
        
        backtrack(0, [])
        print(res)
        return res
