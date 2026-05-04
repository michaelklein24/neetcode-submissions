# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def postorderTraversal(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            leftHeight = postorderTraversal(node.left)
            rightHeight = postorderTraversal(node.right)

            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        
        postorderTraversal(root)

        return maxDiameter