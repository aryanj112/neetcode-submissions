class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        res = 0
        l = r = 0

        while r < len(s):
            if s[r] in visit:
                while s[r] in visit:
                    visit.remove(s[l])
                    l += 1
            res = max(r-l + 1, res)
            visit.add(s[r])
            r += 1
        return 1 if len(s) == 1 else res