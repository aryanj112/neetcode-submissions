class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.keyNode = {}
        self.cap = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def remove(self, node):
        node.prev.next = node.next    
        node.next.prev = node.prev

    def insertAtTail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail  # UNDERSTAND THIS

    def get(self, key: int) -> int:
        res = -1
        if key in self.keyNode:
            currNode = self.keyNode[key]
            res = currNode.val
            self.remove(currNode)
            self.insertAtTail(currNode)
        return res

    def put(self, key: int, value: int) -> None:
        currNode = None
        if key in self.keyNode:
            currNode = self.keyNode[key]
            currNode.val = value
            self.remove(currNode)
        else:
            currNode = Node(key, value)
            self.keyNode[key] = currNode            
        self.insertAtTail(currNode)

        if len(self.keyNode) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.keyNode[lru.key]

