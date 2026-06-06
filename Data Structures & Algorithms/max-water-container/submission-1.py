class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = -1
        
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            if curr_area > max_area:
                max_area = curr_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area