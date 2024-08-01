# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a = head
        
        prev = ListNode(0)
        res = prev
        while(a!=None):
            if(a.val != val):
                newnode = ListNode(a.val)
                prev.next = newnode
                prev = prev.next
            a = a.next
                
        return res.next
