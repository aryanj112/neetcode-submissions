# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        h2 = fast
        curr = h1 = head

        while h1 and h2:
            h1 = h1.next
            curr.next = h2
            curr = curr.next
            h2 = h2.next
            curr.next = h1
            curr = curr.next
