# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right= self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


"""
preorder: root, left, right
inorder: left, root, right

We should be able to build trees recursively
First element in preorder is guaranteed to be the root
We know that all elements to the left of first element in inorder list will be in left subtree
We know that all elements to the right of first element in inorder list will be in right subtree
"""