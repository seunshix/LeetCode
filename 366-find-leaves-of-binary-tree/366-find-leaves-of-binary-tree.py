# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = collections.defaultdict(list)
        
        def height(node, layer):
                if not node:
                    return layer
                
                leftHeight =  height(node.left, layer)               
                rightHeight = height(node.right, layer)                
                
                layer = max(leftHeight, rightHeight)                
                                
                leaves[layer].append(node.val)
                return layer + 1
        
        height(root, 0)
        return leaves.values()
        