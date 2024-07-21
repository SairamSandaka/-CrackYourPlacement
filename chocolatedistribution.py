class Solution:

    def findMinDiff(self, A,N,M):

        # code here

        A.sort()
        j = 0
        i = M-1
        mini = float('inf')
        while(i<len(A)):
            mini = min(mini,(A[i]-A[j]))
            i+=1
            j+=1
        return mini
