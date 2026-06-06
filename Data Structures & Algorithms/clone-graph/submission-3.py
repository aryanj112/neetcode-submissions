"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}
        
        def dfs(n1):
            if not n1:
                return
            if n1 in hashMap:
                return hashMap[n1]
            copy = Node(n1.val)
            hashMap[n1] = copy
            for nei in n1.neighbors:
                hashMap[nei] = dfs(nei)
                copy.neighbors.append(hashMap[nei])
            return copy

        return dfs(node)