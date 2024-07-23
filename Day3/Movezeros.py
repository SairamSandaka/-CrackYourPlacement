class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        zero = 0
        for i in range(len(nums)):
            if(nums[i]==0 and count==0):
                zero = i
                count+=1
            if(nums[i]!=0):
                temp = nums[i]
                nums[i] = nums[zero]
                nums[zero] = temp
                zero+=1

        
