# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA = lenB = 0
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next

        # now just find the longer one and label as l1 and shorter as l2
        l1 = l2 = len1 = len2 = None
        if lenA > lenB:
            l1, len1 = headA, lenA
            l2, len2 = headB, lenB
        else:
            l1, len1 = headB, lenB
            l2, len2 = headA, lenA
        
        while len1 > len2:
            l1 = l1.next
            len1 -=1
        
        for i in range(len1):
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
        return ListNode(0)