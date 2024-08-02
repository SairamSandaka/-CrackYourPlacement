'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self, head):
        # Convert linked list to list
        a = head 
        l = []
        while a is not None:
            l.append(a.data)
            a = a.next

        # Traverse list from end to start and keep track of max values
        max_from_right = float('-inf')
        for i in range(len(l) - 1, -1, -1):
            if l[i] >= max_from_right:
                max_from_right = l[i]
            else:
                l[i] = -1  # Mark elements to be removed

        # Rebuild linked list with required nodes
        a = head
        i = 0
        prev = None
        while a is not None and i < len(l):
            if l[i] != -1:
                if prev is None:
                    head = a
                else:
                    prev.next = a
                prev = a
            a = a.next
            i += 1

        # Ensure the new linked list ends correctly
        if prev is not None:
            prev.next = None
        
        return head
