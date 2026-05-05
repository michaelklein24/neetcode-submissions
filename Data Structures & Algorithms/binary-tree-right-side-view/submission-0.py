# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def bfs(node: Optional[TreeNode], level: int):
            if not node:
                return

            if level > len(result) - 1:
                result.append(-101)
            
            result[level] = node.val
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        bfs(root, 0)
        return result
        