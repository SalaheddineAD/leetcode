# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next ==None:
            return None
        fast = head.next.next
        slow = head
        i=0
        while fast != None:
            fast=fast.next
            i+=1
            if i%2==0:
                slow=slow.next

        slow.next = slow.next.next
        return head