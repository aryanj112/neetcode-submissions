class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashMap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashMap[tuple(count)].append(s)
        print (hashMap)
        
        for key, value in hashMap.items():
            res.append(value)

        return res
