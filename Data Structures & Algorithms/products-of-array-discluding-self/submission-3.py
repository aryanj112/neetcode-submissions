class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = n
            prefix[i] = prefix[i-1] * n

        print(prefix)
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
                continue
            postfix[i] = postfix[i + 1] * nums[i]

        print(postfix)
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
                continue
            if i == len(nums) - 1:
                res.append(prefix[i-1])
                continue
            res.append(prefix[i-1] * postfix[i+1])
        return res
        


        