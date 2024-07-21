class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        k=0
        while(k<len(nums)):
            if(nums[k]==0):
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp 
                i+=1
            k+=1
        k = i
        while(k<len(nums)):
            if(nums[k]==1):
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp 
                i+=1
            k+=1
        
        
