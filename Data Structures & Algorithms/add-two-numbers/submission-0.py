# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy variable 
        # carry
        # pointers to the l1 and l2 
        # making a new output will require space which the max of m and n

        curr = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry

            if val > 9:
                val = val % 10
                carry = 1
            else: 
                carry = 0
            
            node = ListNode(val,None)
            curr.next = node
            curr = curr.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next        
        return dummy.next


                

