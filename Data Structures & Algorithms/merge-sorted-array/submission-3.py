class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        back = m + n - 1
        curr1 = m - 1
        curr2 = n - 1

        while curr1 >= 0 and curr2 >= 0:
            print("before,",nums1, "back:", back, "curr1", curr1, "curr2", curr2)
            if curr2 >= 0 and nums1[curr1] > nums2[curr2]:
                temp = nums1[curr1]
                nums1[curr1] = nums1[back]
                nums1[back] = temp
                back -= 1
                curr1 -= 1
            else:
                nums1[back] = nums2[curr2]
                back -= 1
                curr2 -= 1
            print("after:", nums1, "back:", back, "curr1", curr1, "curr2", curr2)

        while curr2 >= 0 and back >= 0:
            nums1[back] = nums2[curr2]
            curr2 -= 1
            back -= 1  