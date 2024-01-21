# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = 0
        second = 0
        
        i=1
        while l1 != None:
            first += int(l1.val)*i
            i *=10
            l1=l1.next
        i=1
        while l2 != None:
            second += int(l2.val)*i
            i *=10
            l2=l2.next
        
        sum = first+second
        lst_sum = str(sum).strip()

        result = ListNode() 
        result_head= result
        
        print(lst_sum)
        for i in lst_sum[::-1]:
            result_head.val = int(i)
            before = result_head
            result_head.next = ListNode()
            result_head = result_head.next

        # result_head = None
        before.next = None
        return result