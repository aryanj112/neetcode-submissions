class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        leng = len(nums)

        ans = [0] * (2 * leng)
        for i, n in enumerate(nums):
            ans[i] = ans[i + leng] = n

        return ans