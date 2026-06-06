class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for n in nums:
            hashMap[n] += 1
        count = [[] for _ in range(len(nums) + 1)]
        for key, value in hashMap.items():
            count[value].append(key)    
        res = []
        for i in range(len(count) - 1, -1, -1):
            if len(res) == k:
                return res
            for elm in count[i]:
                res.append(elm)
        return res
