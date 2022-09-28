# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].append([node.left.val, "L"])
                graph[node.left.val].append([node.val, "U"])
                
                queue.append(node.left)
            
            if node.right:
                graph[node.val].append([node.right.val, "R"])
                graph[node.right.val].append([node.val, "U"])
                
                queue.append(node.right)
                
        queue = collections.deque([(startValue, "")])
        seen = set()
        
        while queue:
            cur_val, cur_path = queue.popleft()
            
            if cur_val in seen:
                continue
            
            seen.add(cur_val)
            
            if cur_val == destValue:
                return cur_path
            
            for child, direction in graph[cur_val]:
                if child not in seen:
                    queue.append((child, cur_path + direction))
                    
        