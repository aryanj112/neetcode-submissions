class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        
        for s in strs:
            hashMap[''.join(sorted(s))].append(s)

        res = []
        for key,value in hashMap.items():
            res.append(value)
        return res

        # hashmap -> a list