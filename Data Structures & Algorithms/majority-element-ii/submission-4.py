class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # n // 3
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

            if len(hashmap) == 3:
                temp = defaultdict(int)
                for key in hashmap.keys():
                    hashmap[key] -= 1
                    if hashmap[key] != 0:
                        temp[key] = hashmap[key]
                hashmap = temp
                
        for key in hashmap.keys():
            hashmap[key] = 0

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
        
        res = []
        
        for key,val in hashmap.items():
            if val > len(nums) // 3:
                res.append(key)
        return res

        