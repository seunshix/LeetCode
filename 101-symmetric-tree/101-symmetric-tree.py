# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val == right.val) and mirror(left.left, right.right) and mirror(left.right, right.left)
        if root is None:
            return True
        return mirror(root.left, root.right)