# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(pNode, qNode):
            if not pNode and not qNode:
                return True
            elif not pNode or not qNode:
                return False
            
            return pNode.val == qNode.val and isSame(pNode.left, qNode.left) and isSame(pNode.right, qNode.right)
                

        return isSame(p, q)
