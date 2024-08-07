class Solution:
    def climbStairs(self, n: int) -> int:
        l = [-1 for i in range(n+1)]
        l[0],l[1]=[1,1]
        for i in range(2,n+1):
            l[i]=l[i-1]+l[i-2]
        return l[n]
