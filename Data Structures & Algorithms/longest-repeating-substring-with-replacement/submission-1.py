class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charHash = {}
        res = 0
        maxF = 1

        for r in range(len(s)):
            charHash[s[r]] = 1 + charHash.get(s[r], 0)
            maxF = max(maxF, charHash[s[r]])
            
            while (r - l + 1) - maxF > k:
                charHash[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res