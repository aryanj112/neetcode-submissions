class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: string of length 0 - 1000
        # output: size of the largest substring

        # edge cases: empty string, only one letter, one letter multiple times

        # go through in one one pass and shrink the window as you go if you find duplicates
        
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res