class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 1
        if(len(nums)==2):
            if(nums[0]==nums[1]):
                return 1
            else:
                return 2
        unq = 0
        nunq = 1
        count = 1
        for i in range(1,len(nums)):
            if(nums[unq]!=nums[i]):
                temp = nums[nunq]
                nums[nunq]=nums[i]
                nums[i]=temp
                unq+=1
                nunq+=1
                count+=1
        return count
            
        
