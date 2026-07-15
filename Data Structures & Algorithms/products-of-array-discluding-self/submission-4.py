class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        postfix = [nums[-1]] * len(nums)
        
        # create a prefix array
        for i, n in enumerate(nums):
            if i == 0:
                continue
            prefix[i] = prefix[i-1] * n
        
        print(prefix)


        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                continue
            postfix[i] = postfix[i+1] * nums[i]
            
        print(postfix)

        res = []

        for i in range(len(nums)):
            num = 0
            if i == 0:
                num = postfix[i+1]
            elif i == len(nums) - 1:
                num = prefix[i-1]
            else:
                num = prefix[i-1] * postfix[i+1] 
            res.append(num)
        print(res)
        return res
