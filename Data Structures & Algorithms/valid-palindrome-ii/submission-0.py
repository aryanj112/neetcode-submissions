class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_valid(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                print("first mismatch", s[l], s[r])
                print(is_valid(l,r-1))
                if not is_valid(l+1,r) and not is_valid(l,r-1):
                    return False
                else:
                    return True
            l += 1
            r -= 1
        return True
