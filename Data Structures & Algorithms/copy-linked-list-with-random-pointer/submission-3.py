"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}

        curr = head
        while curr:
            newNode = Node(curr.val, None, None)
            oldToNew[curr] = newNode
            curr = curr.next
        
        for key,value in oldToNew.items():
            print(key.val, value.val)

        curr = head
        while curr:
            if curr.next:
                oldToNew[curr].next = oldToNew[curr.next]
            else:
                oldToNew[curr].next = None
            if curr.random:
                oldToNew[curr].random = oldToNew[curr.random]
            else:
                oldToNew[curr].random = None
            curr = curr.next

        return oldToNew[head] if head else None