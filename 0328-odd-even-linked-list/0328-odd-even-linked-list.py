# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next ==None:
            return head
        odd = head
        even = head.next
        tmp_odd = odd
        tmp_even = even
        
        i=1
        tmp = even
        while tmp.next != None:
            tmp = tmp.next
            if i%2 !=0:
                tmp_odd.next = tmp
                tmp_odd = tmp
            else:
                tmp_even.next = tmp
                tmp_even = tmp
            i+=1
        tmp_odd.next =even
        tmp_even.next =None
        return odd
            