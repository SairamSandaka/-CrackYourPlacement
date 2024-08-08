class Solution:
    def isPossible(self,a, b, n, k):
    # Your code goes here
        a.sort()
        b.sort()
        b = b[::-1]
    
        for i in range(n):
            if(a[i]+b[i] < k):
                return False
        return True
