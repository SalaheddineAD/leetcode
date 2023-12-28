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
    public ListNode middleNode(ListNode head) {
        if(head.next==null){
            return head;
        }
        int keep_track=2;
        ListNode result=head.next;
        head=head.next;
        while(head.next!=null){
            keep_track+=1;
            if(keep_track%2==0){
                result=result.next;
                System.out.println(result.val);
            }
            head=head.next;
        }
        return result;
    }
}