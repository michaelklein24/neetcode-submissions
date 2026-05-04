# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0
        
        def bfs(node: Optional[TreeNode], height: int):
            if not node:
                return
            height += 1

            nonlocal maxHeight
            maxHeight = max(maxHeight, height)

            bfs(node.left, height)
            bfs(node.right, height)

        bfs(root, 0)

        return maxHeight