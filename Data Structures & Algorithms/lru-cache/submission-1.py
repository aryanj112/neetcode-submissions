class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # head -> LRU (where we delete from if capacity is high)
    # tail -> MRU (where we move when operations are done)
    # when we remove from the head we want to make no more node point to 
    # it and then do del hashMap[key] (when we delete we will not know the
    # key so we will need to figure that out (store the key as well in 
    # the node class)

    def __init__(self, capacity: int):
        self.keyNode = {}
        self.cap = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        
        # init a hashmap that holds stores key-node(l,r,v, k)
        # init a head and tail pointer
            # tail will be the most recently used and our head 
            # will be the LRU
    
    def remove(self, node):
        node.prev.next = node.next    
        node.next.prev = node.prev

    def insertAtTail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


    def get(self, key: int) -> int:
        # go into the hashmap and get the node with the key: key
        # store the value at that node or -1
        # move the node that corresponds to the key to the end of the list 
        res = -1
        if key in self.keyNode:
            currNode = self.keyNode[key]
            res = currNode.val
            self.remove(currNode)
            self.insertAtTail(currNode)
        return res

    def put(self, key: int, value: int) -> None:
        # check if its in the hashmap 
            # if in then update the value and move to the end of the list
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

