# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node: TreeNode, currMax: int):
            if not node:
                return
            
            nonlocal result

            if currMax <= node.val:
                result += 1
                currMax = node.val

            dfs(node.left, currMax)
            dfs(node.right, currMax)
        
        dfs(root, -101)
        return result