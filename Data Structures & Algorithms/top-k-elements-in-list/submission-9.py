import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for n in nums:
            dic[n] += 1

        arr = [[] for _ in range(len(nums) + 1)]
        
        for num, count in dic.items():
            arr[count].append(num)
        
        print(arr)

        res = []
        curr = []
        for i in range(len(nums), -1 , -1):
            if arr[i] != []:
                res += arr[i]
            if len(res) == k:
                return res
            print(i)

        return res
