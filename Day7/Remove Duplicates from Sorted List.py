# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        prev = ListNode(0)
        a = head
        while(a!=None):
            if(a.val in dic):
                prev.next = a.next
            else:
                dic[a.val]=0
                prev= a
            a = a.next
        return head
