class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        hashMap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        curr = ""
        def dfs(s):
            nonlocal curr
            if s == "":
                res.append(curr)
                return

            for letter in hashMap[s[0]]:
                curr += letter
                dfs(s[1:])
                curr = curr[:-1]

        dfs(digits)


        return res