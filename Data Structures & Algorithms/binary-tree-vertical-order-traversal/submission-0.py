# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashMap = {} # col to list of values in it
        if not root:
            return []
        # want to do a breath first search because it maintains top to bottom
        # and left to right 

        q = collections.deque()
        q.append((0,root))
        minCol = maxCol = 0
        while q:
            for _ in range(len(q)):
                col, node = q.popleft()
                if col not in hashMap:
                    hashMap[col] = []
                hashMap[col].append(node.val)
                minCol = min(col, minCol)
                maxCol = max(col, maxCol)
                if node.left:
                    q.append((col-1,node.left))
                if node.right:
                    q.append((col+1,node.right))
        res = []
        for i in range(minCol, maxCol + 1, 1):
            res.append(hashMap[i])
        return res