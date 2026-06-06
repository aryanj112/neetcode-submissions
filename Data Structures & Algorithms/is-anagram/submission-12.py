class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = defaultdict(int)        
        tHash = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sHash[s[i]] += 1
            tHash[t[i]] += 1

        return sHash == tHash