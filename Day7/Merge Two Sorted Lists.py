# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode(0)
        res = newlist
        while(list1!=None and list2!=None):
            if(list1.val<list2.val):
                newnode = ListNode(list1.val)
                newlist.next = newnode
                newlist = newlist.next
                list1 = list1.next  
            else:
                newnode = ListNode(list2.val)
                newlist.next = newnode
                newlist = newlist.next
                list2 = list2.next  
        if(list1!=None):
            while(list1!=None):
                newnode = ListNode(list1.val)
                newlist.next = newnode
                newlist = newlist.next
                list1 = list1.next  
        if(list2!=None):
            while(list2!=None):
                newnode = ListNode(list2.val)
                newlist.next = newnode
                newlist = newlist.next
                list2 = list2.next  
        return res.next
