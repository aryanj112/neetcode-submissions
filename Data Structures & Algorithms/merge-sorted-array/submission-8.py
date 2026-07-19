class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        back = m + n - 1
        curr1 = m - 1
        curr2 = n - 1

        while curr1 >= 0 and curr2 >= 0:
            if nums1[curr1] > nums2[curr2]:
                nums1[back] = nums1[curr1]
                nums1[curr1] = 0
                curr1 -= 1
            else:
                nums1[back] = nums2[curr2]
                curr2 -= 1
            back -= 1

        while curr2 >= 0 and back >= 0:
            nums1[back] = nums2[curr2]
            curr2 -= 1
            back -= 1  