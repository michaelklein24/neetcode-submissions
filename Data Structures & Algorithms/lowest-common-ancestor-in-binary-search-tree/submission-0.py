# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]

        a, b = p, q
        if p.val > q.val:
            a, b = b, a

        while True:
            node = stack.pop()
            if node.val == a.val:
                return a
            
            if node.val == b.val:
                return b
            
            if a.val < node.val < b.val:
                return node
            
            if a.val < node.val and b.val < node.val:
                stack.append(node.left)
            
            if a.val > node.val and b.val > node.val:
                stack.append(node.right)
            
        