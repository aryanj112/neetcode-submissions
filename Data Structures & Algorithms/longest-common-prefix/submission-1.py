class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = float('inf')

        for s in strs:
            min_len = min(min_len, len(s))

        for idx in range(min_len):
            char = strs[0][idx]
            
            for s in strs:
                if s[idx] != char:
                    return res
            
            res += char
        
        return res