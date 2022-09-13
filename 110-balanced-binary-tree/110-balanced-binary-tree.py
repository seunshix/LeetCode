# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        BalancedStatusWithHeight = collections.namedtuple("BalancedStatusWithHeight", ('balanced', 'height'))
        
        def check_balanced(root):
            if not root:
                return BalancedStatusWithHeight(balanced = True, height = -1)
            
            left_result, right_result = check_balanced(root.left), check_balanced(root.right)
            
            if not left_result.balanced:
                return left_result
            if not right_result.balanced:
                return right_result
            
            is_balanced = abs(left_result.height - right_result.height) <=1
            height = 1 + max(left_result.height, right_result.height)
            
            return BalancedStatusWithHeight(is_balanced, height)
        
        return check_balanced(root).balanced