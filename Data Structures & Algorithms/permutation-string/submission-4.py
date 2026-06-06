class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        hashS1 = {}
        hashS2 = {}
        
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            hashS1[s1[i]] = 1 + hashS1.get(s1[i], 0)
            hashS2[s2[i]] = 1 + hashS2.get(s2[i], 0)

        for r in range(len(s1), len(s2), 1):
            if hashS1 == hashS2:
                return True
            hashS2[s2[r]] = 1 + hashS2.get(s2[r], 0)

            hashS2[s2[l]] = hashS2.get(s2[l]) - 1

            if hashS2[s2[l]] == 0:
                del hashS2[s2[l]]
            l += 1
        return hashS1 == hashS2