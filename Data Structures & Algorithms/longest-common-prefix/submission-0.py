class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # bat -> b, ba, bat

        # iterate through the array k times and each time see if each word in
        # the array starts with that value (k is the number of possible prefixes in
        # the first word)  -> O(n*k) solutions
        
        # Places to improve
        # Notice that the longest prefix can only be as long as the shortest string
        # Given this we can optimize by first sorting and then going through the 
        # array -> log(n) + k * n -> O(k * n)
        # if we stop it at the shortest string then we actually dont need to sort

        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


