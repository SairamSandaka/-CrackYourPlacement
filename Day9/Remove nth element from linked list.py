# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = head
        b= head
        len = 0
        prev = None
        count=1
        while(b!=None):
            len+=1
            b=b.next
        if(n==len):
            return head.next
        while(head!=None):
            if(count==len-n+1):
                if(prev == None):
                    return 
                prev.next = head.next
                prev = prev.next
                break
            else:
                prev = head
                head = head.next
                
                count+=1
        return a
        
