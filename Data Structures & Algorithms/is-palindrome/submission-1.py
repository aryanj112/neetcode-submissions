class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        
        limit = len(new_s) // 2
        
        i = 0
        j = len(new_s) - 1

        while i <= limit and limit > 0:
            if(new_s[i] != new_s[j]):
                return False
            i += 1
            j -= 1

        return True
