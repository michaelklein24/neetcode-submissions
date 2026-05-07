# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        result = float('-inf')

        def inorderTraversal(node: Optional[TreeNode]):
            nonlocal curr
            nonlocal result
            nonlocal k

            if not node:
                return
            
            inorderTraversal(node.left)
            
            curr += 1
            if curr == k:
                result = node.val
                return
            
            inorderTraversal(node.right)
        
        inorderTraversal(root)
        return result