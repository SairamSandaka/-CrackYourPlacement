# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,l):
        curr = l
        prev = None
        next = None
        while(curr!=None):
            next = curr.next
            curr.next  = prev 
            prev = curr
            curr = next
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        print(l1.val,l2.val)
        carry = 0
        res = ListNode(0)
        ans = res
        while(l1!=None and l2!=None):
            new = ListNode((l1.val+l2.val+carry)%10)
            res.next = new
            carry = (l1.val+l2.val+carry)//10
            res = res.next
            l1 = l1.next
            l2 = l2.next
        if(l1!=None):
            while(l1!=None):
                new = ListNode((l1.val+carry)%10)
                carry = (l1.val+carry)//10
                res.next = new
                res = res.next
                l1 = l1.next
        if(l2!=None):
            while(l2!=None):
                new = ListNode((l2.val+carry)%10)
                carry = (l2.val+carry)//10
                res.next = new
                res = res.next
                l2 = l2.next
            
        if(carry!=0):
            new = ListNode(carry)
            res.next = new
        return self.reverse(ans.next)
