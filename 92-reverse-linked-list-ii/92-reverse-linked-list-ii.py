# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
     # The idea is to go through the linked list and when we find the nodes we need to swap, then add them to a list. 
	 # Then use two pointers while going through this list and swap their respetive values. 
	 # Time: O(N), Space: O(N)
        
        # Create an array/map to store the found nodes.
        hashMap = []
        # Create a sentinel/dummy at the head of the list.
        dummy = ListNode(0,head)
        current = dummy.next
        
        # Initialise a count 'value' to see which node we're on.
        count = 1
        # Keep going until count is less than the right value, we don't need to go any further after.
        while count <= right:
            # Check if 'count' is within our given boundries.
            if count >= left and count <= right:
                # If it is, then add the current node to the list.
                hashMap.append(current)
            
            # Then move to the next node, and increment count to signify we're moving to the next node as well.
            current = current.next
            count += 1
            
        # After this, a list with our needed nodes is found.
        
        # Initialise two pointers.
        left, right = 0, len(hashMap) - 1
        while left < right:
            # For ease of reading, get the left and right nodes from the list.
            first  = hashMap[left]
            second = hashMap[right]
            # Then swap their values.
            first.val, second.val = second.val, first.val
            # Then increment and decrement the counters since we're ready to move onto the next set of nodes.
            left += 1
            right -= 1
        
        # Then just return the list.
        return dummy.next