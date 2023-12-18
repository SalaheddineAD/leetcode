/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void helper(ListNode list,ListNode result){
        if(list!=null){
            helper(list.next,result);
            ListNode tmp_result=result;
            while(tmp_result.next!=null){
                tmp_result=tmp_result.next;
            }
            tmp_result.next=new ListNode();
            tmp_result=tmp_result.next;
            tmp_result.val=list.val;
        }
    }
    public ListNode reverseList(ListNode head) {
        ListNode result=new ListNode();
        helper(head,result);
        return result.next;
        
    }
}