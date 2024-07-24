class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        s = 0
        count = 0
        dic[s] = 1
        for i in range(len(nums)):
            s += nums[i]
            if(s-k in dic):
                count+=dic[s-k]
            if(s not in dic):
                dic[s]=1
            else:
                dic[s]+=1
        return count
            
