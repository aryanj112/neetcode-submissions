class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # [1,2,4,6]
        # pre = [1,2,8,48]
        # post [48,48,24,6]
        res = [1] * N
        # make the pre-array
        prefix = [1] * N
        curr = 1
        for i in range(N):
            curr = nums[i] * curr
            prefix[i] = curr
        
        # build postfix
        postfix = [1] * N

        curr = 1
        for i in range(N-1,0,-1):
            curr = nums[i] * curr
            postfix[i] = curr
        print(postfix)

        for i in range(N):
            left = 1
            right = 1
            if i - 1 >= 0:
                left = prefix[i-1]
            if i + 1 < N:
                right = postfix[i+1]
            res[i] = left * right
        
        return res