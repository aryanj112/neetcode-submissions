class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n not in hashSet:
                hashSet.add(n)
            else:
                return True
        return False
