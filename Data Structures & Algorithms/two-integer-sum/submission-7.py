class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # num to index

        for i, n in enumerate(nums):
            need = target - n
            if need in hashMap:
                return [hashMap[need],i]
            hashMap[n] = i

        return []