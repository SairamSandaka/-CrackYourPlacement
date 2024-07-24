class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=len(nums)//2
 
        if(len(nums)%2!=0):
            a+=1
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for i in dic:
            if(dic[i]>=a):
                return i
        
