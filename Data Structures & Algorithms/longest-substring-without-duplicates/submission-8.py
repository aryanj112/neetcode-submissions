class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        res = 0
        left = right = 0

        while right < len(s):
            if s[right] in visit:
                while s[left] != s[right] and s[right] in visit:
                    visit.remove(s[left])
                    left += 1
                left += 1
            res = max(right-left + 1, res)
            visit.add(s[right])
            right += 1

        return 1 if len(s) == 1 else res
    
    # au
    # |
    #  |