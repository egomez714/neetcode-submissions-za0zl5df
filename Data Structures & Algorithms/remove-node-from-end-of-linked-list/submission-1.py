# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # creates dummy to start 1 before head
        dummy = ListNode(0,head)
        left = dummy
        right = head
        # creates the offset between Left and right (moves right n times)
        while n > 0 and right:
            right = right.next
            n-=1
        # while right is not at the end of the list move l and right 
        while right:
            left = left.next
            right = right.next
        # deletes the next node by moving next pointer to the one after it
        left.next = left.next.next

        # returns dummy next pointing to head of list 
        return dummy.next
        
