class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        num_s = {}
        num_t = {}
        
        for i in range(len(s)):
            if num_s.get(s[i]) == None:
                num_s[s[i]] = 1
            else:
                num_s[s[i]] += 1

            if num_t.get(t[i]) == None:
                num_t[t[i]] = 1
            else:
                num_t[t[i]] += 1

        return num_s == num_t
        