class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        freqs = defaultdict(list)
        for num, cnt in count.items():
            freqs[cnt].append(num)
        
        print(freqs)
        
        res = []
        for i in range(len(nums),-1,-1):
            res += freqs[i]
            if len(res) == k:
                return res
        return res