# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
    
        def goodCounter(curr, maxVal):
            nonlocal res
            currMax = maxVal

            if not curr:
                return
            if curr.val >= currMax:
                currMax = curr.val
                res += 1
            
            goodCounter(curr.left, currMax)
            goodCounter(curr.right, currMax)

        goodCounter(root, root.val - 1)

        return res