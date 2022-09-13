# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if val < root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    root.left = self.insertIntoBST(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    root.right = self.insertIntoBST(root.right, val)
            else:
                raise ValueError("Duplicate entries not allowed")
        if not root:
            return TreeNode(val)
        return root
                    
        