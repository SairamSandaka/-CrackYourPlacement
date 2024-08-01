class node:
    def __init__(self):
        self.data = None
        self.next = None


class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        a = 0
        MOD = 10**9 + 7
        b = 0
        a1 = first
        a2 = second
        
        while(a1!=None):
            a = (a * 10 + a1.data) % MOD
            a1=a1.next
        while(a2!=None):
            b = (b * 10 + a2.data) % MOD
            a2=a2.next
            
        ans = (a*b)%MOD
        
            
        return ans
