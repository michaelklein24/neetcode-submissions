# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(1, root)]
        maxHeight = 0

        while stack:
            d, node = stack.pop()

            if node:
                maxHeight = max(maxHeight, d)
                stack.append((d + 1, node.left))
                stack.append((d + 1, node.right))
        
        return maxHeight