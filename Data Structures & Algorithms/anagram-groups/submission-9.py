class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            curr_str = [0] * 26
            for c in s:
                curr_str[ord(c) - ord('a')] += 1
            hashMap[tuple(curr_str)].append(s)
        return list(hashMap.values())