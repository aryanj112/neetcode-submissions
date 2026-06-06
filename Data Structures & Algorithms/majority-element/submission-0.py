class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # [6, 6, 6, 3]    > 2
        # [1, 3, 3, 3, 5] 5//2 = 2 < so 3+

        # iterate through the list and keep a hashmap and then from the hashmap
        # find the largest value O(n) time and O(n) space
        # iterating to develop the hashmap    O(n) 
        # go through the hashmap is O(n)
        # and find the largest value      
        # [1, 3, 3, 3, 5]
        # 1 -> 1
        # 3 -> 3
        # 5 -> 5
        '''
        Since we are looking to complete this problem in O(1) space we need to 
        consider how many possible values there can be 

        since we need a majority we really only care about one value

        5 red balloons and 4 blue ballons and you see a random combination of them
        one by one how do you know which color is the majority. 

        For every blue balloon you see you pop a red. 
        
        [1, 2, 2, 2, 3]
            |
        
        if n != curr:
            curr_count -= 1
            if curr_count == 0:
                curr = n
                curr_count = 1
        else:
            curr_count += 1

        2 : 2


        '''
        curr, curr_count = nums[0], 0
        for n in nums:
            if n != curr:
                curr_count -= 1
                if curr_count == 0:
                    curr = n
                    curr_count = 1
            else:
                curr_count += 1
        
        # curr_count = 0
        # for n in nums:
        #     if n == curr:
        #         curr_count += 1
        # if curr_count == len(nums) // 2
        return curr

