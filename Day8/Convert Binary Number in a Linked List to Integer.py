# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = head
        res = ''
        while(a!=None):
            res += str(a.val)
            a = a.next
        return int(res,2)
        
