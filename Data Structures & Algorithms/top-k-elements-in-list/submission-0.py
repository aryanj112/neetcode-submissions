class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap to store occurances of each value in first pass
        freq = [[] for i in range(len(nums) + 1)] # tuff syntax

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n) # freq[c] gives us a list and we will append to a list
        
        print(freq)

        res = []
        for i in range(len(nums) + 1):
            index = len(nums) - i
            print(index)
            for n in freq[index]:
                res.append(n)
                if len(res) == k:
                    return res