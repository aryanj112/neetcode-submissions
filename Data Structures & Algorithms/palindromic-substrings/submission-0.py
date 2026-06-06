class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(0,len(s), 1):
            for j in range(2):
                # j = 0 = even | j = 1 = odd
                l = i - j
                r = i + 1
                if j == 1:
                    res += 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1
                    r += 1
                    l -= 1
        return res