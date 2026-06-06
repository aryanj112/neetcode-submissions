class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s

        res = ""
        
        # find all the odd palindromes
        i = 1
        while i < len(s):
            l, r = i-1, i+1
            curr = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l] + curr + s[r]
                l -= 1
                r += 1

            if len(curr) > len(res):
                res = curr
                print(res)

            i += 1
        
        il, ir = 0, 1
        while ir < len(s):
            if s[il] != s[ir]:
                il += 1
                ir += 1
                continue
            
            l, r = il - 1, ir + 1
            curr = s[il] + s[ir]
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l] + curr + s[r]
                l -= 1
                r += 1

            if len(curr) > len(res):
                res = curr
                print(res)

            il += 1 
            ir += 1

        return res