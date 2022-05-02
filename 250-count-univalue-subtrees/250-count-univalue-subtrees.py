# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.count = 0
        self.isUni(root)

        return self.count
    
    def isUni(self, node):
        if node.left is None and node.right is None:
            self.count += 1
            return True
        isUni = True
        
        if node.left is not None:
            isUni = self.isUni(node.left) and isUni and node.left.val == node.val
            
        if node.right is not None:
            isUni = self.isUni(node.right) and isUni and node.right.val == node.val
            
        self.count += isUni
        return isUni
    