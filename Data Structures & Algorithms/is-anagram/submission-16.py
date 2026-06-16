class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = defaultdict(int)
        tDic = defaultdict(int)
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sDic[s[i]] += 1
            tDic[t[i]] += 1

        return sDic == tDic

