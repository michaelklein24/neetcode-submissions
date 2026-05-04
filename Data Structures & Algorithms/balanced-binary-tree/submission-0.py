# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def getHeight(node: Optional[TreeNode]) -> height:
            nonlocal balanced

            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            if abs(leftHeight - rightHeight) > 1:
                balanced = False
            
            return 1 + max(leftHeight, rightHeight)

        getHeight(root)
        return balanced