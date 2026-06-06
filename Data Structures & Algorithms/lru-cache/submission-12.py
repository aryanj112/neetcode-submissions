class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keyNode = {} # maps a key to a linked list node
        self.capacity = capacity
        self.curr = 0 
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head 
    
    def addToEnd(self, key, value):
        node = Node(key,value)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        self.keyNode[key] = node

    def addToStart(self, key, value):
        node = Node(key,value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        self.keyNode[key] = node
    
    def removeFromStart(self):
        node = self.head.next
        del self.keyNode[node.key]
        self.head.next = node.next
        node.next.prev = self.head

    def remove(self, key):
        node = self.keyNode[key]
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        del self.keyNode[key]

    def printLL(self):
        curr = self.head
        print("printing current linked list")
        while curr:
            if curr.val:
                print(curr.val)
            curr = curr.next

    def get(self, key: int) -> int:
        res = -1
        if key in self.keyNode:
            res = self.keyNode[key].val
            self.remove(key)
            self.addToEnd(key,res)
        self.printLL()
        print("res:",res)
        return res

    def put(self, key: int, value: int) -> None:
        print("keynode", self.keyNode)
        if key in self.keyNode:
            self.keyNode[key].val = value
            self.remove(key)
            self.addToEnd(key,value)
        else:
            self.curr += 1
            if self.curr > self.capacity:
                self.removeFromStart()
                self.curr -= 1
            self.addToEnd(key,value)
        self.printLL()