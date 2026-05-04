# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSub(rootNode, subNode):
            
            if not rootNode and not subNode:
                return True
            
            if not rootNode or not subNode:
                return False
            
            return rootNode.val == subNode.val and isSub(rootNode.left, subNode.left) and isSub(rootNode.right, subNode.right)

        stack = [root]

        while stack:
            node = stack.pop()

            if isSub(node, subRoot):
                return True
            else:
                stack.append(node.left) if node.left else None
                stack.append(node.right) if node.right else None
        
        return False
