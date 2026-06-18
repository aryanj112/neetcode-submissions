class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = nex = 0

        while nex < len(nums):
            if nums[nex] == val:
                nex += 1
                continue
            
            if nums[curr] == val:
                nums[curr] = nums[nex]
                nums[nex] = val
            curr += 1
            nex += 1
        return curr