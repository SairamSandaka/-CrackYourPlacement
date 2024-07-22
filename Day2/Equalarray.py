class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        count = 0
        for i in nums:
            count = count + abs(median-i)
        return count

        
