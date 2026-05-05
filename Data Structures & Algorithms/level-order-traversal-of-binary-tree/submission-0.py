# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def bfs(node: Optional[TreeNode], level: int):
            nonlocal result

            if not node:
                return
            
            if level > len(result) - 1:
                result.append([])
            
            result[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        bfs(root, 0)
        return result
