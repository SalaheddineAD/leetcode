# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sum_lst =[]
        
        #get len of linkedList
        fast = head
        slow = head
        n=0
        while fast!= None:
            fast = fast.next
            if n%2==0:
                slow= slow.next
            n+=1
        #Initialiing list
        fast = head
        i=0
        while i<n/2:
            sum_lst.append(fast.val)
            fast= fast.next
            i+=1
        i=int(n/2)-1
        # completing list
        while fast!=None:
            sum_lst[i]+=fast.val
            fast=fast.next
            i-=1
        # print(sum_lst) 
        return max(sum_lst)