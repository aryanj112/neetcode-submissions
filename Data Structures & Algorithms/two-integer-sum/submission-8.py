class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i,n in enumerate(nums):
            second = target - n
            if second in hashMap:
                return [hashMap[second],i]
            hashMap[n] = i