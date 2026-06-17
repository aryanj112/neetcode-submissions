class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map the anagram dicts to the string list
        dic = defaultdict(list)

        for s in strs:
            s_dic = defaultdict(int)
            s_arr = [0] * 26
            for c in s:
                s_arr[ord(c) - ord('a')] += 1
            dic[tuple(s_arr)].append(s)
        
        res = []
        for array in dic.values():
            res.append(array)

        return res
