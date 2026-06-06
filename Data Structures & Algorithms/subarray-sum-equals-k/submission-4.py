class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix, res = 0, 0
        hashMap = {0:1}
        for n in nums:
            prefix += n
            target = prefix - k
            res += hashMap.get(target, 0)
            hashMap[prefix] = hashMap.get(prefix, 0) + 1

        return res