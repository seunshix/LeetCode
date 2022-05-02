# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def arraytoBT(left, right):
            nonlocal preorderIndex
            
            if left> right: return None
            
            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)
            
            preorderIndex += 1
            
            root.left = arraytoBT(left, inorderIndexMap[rootValue] - 1)
            root.right = arraytoBT(inorderIndexMap[rootValue] + 1, right)
            return root
        
        preorderIndex = 0
        
        inorderIndexMap = {}
        for index, value in enumerate(inorder):
            inorderIndexMap[value] = index
        return arraytoBT(0, len(preorder) - 1)
        