# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        
        result =  1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
       
        return result