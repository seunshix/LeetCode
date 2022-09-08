# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:      
        dummy = tail = ListNode()
        
        while list1 and list2:
            print("List1", list1)
            print("List2", list2)
            print("Dummy", dummy)
            print("Tail", tail)
            print()
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            
            else:
                tail.next, list2 = list2, list2.next
                
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
                
            