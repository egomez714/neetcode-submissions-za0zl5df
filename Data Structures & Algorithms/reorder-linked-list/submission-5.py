# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp
        curr = head
        second = prev
        while second:
            tmp1 = curr.next
            tmp2 = second.next
            curr.next = second
            second.next = tmp1
            curr = tmp1
            second = tmp2