class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        count = defaultdict(int)
        res = []  


        for n in nums:
            hashMap[n] += 1
            if len(hashMap) > 2:
                newHashMap = defaultdict(int)
                for key, value in hashMap.items():
                    value = value - 1
                    if value > 0:
                        newHashMap[key] = value
                hashMap = newHashMap   
        
        for n in nums:
            for key in hashMap.keys():
                if n == key:
                    count[n] += 1

        for key in hashMap.keys():
            if count[key] > (len(nums) // 3):
                res.append(key)

        return res