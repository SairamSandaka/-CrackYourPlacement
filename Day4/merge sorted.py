class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        l = []
        while(i<m and j<n):
            if(nums1[i]<nums2[j]):
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        
        if(i<m):
            while(i<m):
                l.append(nums1[i])
                i+=1
        if(j<n):
            while(j<n):
                l.append(nums2[j])
                j+=1
        print(l)
        for k in range(len(l)):
            nums1[k] = l[k]

        
