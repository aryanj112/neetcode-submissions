class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums has len n and we want to create ans double the length of nums where 
        # ans i and i + n == nums[i]

        # 0, 1, 2, 3     0, 1, 2, 3, 4, 5, 6, 7
        # 1, 2, 3, 4 -> [1, 2, 3, 4, 1, 2, 3, 4]
        
        # len(nums) = 4

        # 0 + 4 = 4
        # ans[0] = 1, ans[4] = 1
        # go through nums and have a hashmap that maps index -> number
        # we can also map n+index to the same number or after ans is created
        # we see if we are past n and then we can start doing whatever index we are 
        # on minus n and check for that in the hashmap

        hashMap = {} # both indexs to value
        length = len(nums)
        res = []
        for i,n in enumerate(nums):
            res.append(n)
            hashMap[i + length] = n

        
        for i in range(length, 2 * length, 1):
            res.append(hashMap[i])
        return res







