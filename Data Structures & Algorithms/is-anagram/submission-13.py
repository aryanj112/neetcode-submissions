class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash, tHash = defaultdict(int), defaultdict(int)

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            sHash[sc] += 1
            tHash[tc] += 1
        return sHash == tHash