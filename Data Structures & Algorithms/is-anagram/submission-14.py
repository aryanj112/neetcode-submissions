class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sArr = [0] * 26
        tArr = [0] * 26

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            sArr[ord(sChar) - ord('a')] += 1
            tArr[ord(tChar) - ord('a')] += 1

        return sArr == tArr
        