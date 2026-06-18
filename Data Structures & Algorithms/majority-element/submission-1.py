class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currN = currC = 0

        for n in nums:
            if n == currN:
                currC += 1
            else:
                currC -= 1
            if currC < 0:
                currC = 0
                currN = n
        
        return currN
