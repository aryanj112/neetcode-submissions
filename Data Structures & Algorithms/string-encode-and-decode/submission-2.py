class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + 'a' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0        
        while i < len(s):
            end = i + 1
            while end < len(s) and s[end] != 'a':
                end += 1
            length = int(s[i:end])
            new_start = end + 1
            new_end = new_start + length
            string = s[new_start:new_end]
            res.append(string)
            i = new_end

        return res
