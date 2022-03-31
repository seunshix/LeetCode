# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        l = 0
        first = head
        while first is not None:
            l += 1
            first = first.next
        l -= n
        first = dummy
        while l > 0:
            l -=1
            first = first.next
            
        first.next = first.next.next
        
        return dummy.next
        
        