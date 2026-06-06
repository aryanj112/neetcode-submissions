class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = (r - l) * min(heights[l], heights[r])

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
        return res