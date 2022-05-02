# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def recurseTree(currentNode):
            nonlocal ans
            if not currentNode:
                return False
            left = recurseTree(currentNode.left)
            right = recurseTree(currentNode.right)
            
            mid = currentNode == p or currentNode == q
            
            if mid + left + right >=2:
                ans = currentNode
            
            return mid or left or right
        recurseTree(root)
        return ans