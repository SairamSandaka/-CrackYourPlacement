# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        count=0
        while(a!=None):
            count+=1
            a=a.next
        b = count//2 + 1
        c = None
        res = head
        while(b>0 and res!=None):
            c = res
            res = res.next
            b-=1
        return c
