class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        dic = {}
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            if(s%k==0):
                if(0 in dic):
                    dic[0]+=1
                    count +=dic[0]
                else:
                    dic[0]=1
                    count +=1
            else:
                if(s%k in dic):
                    count+=dic[s%k]
                    dic[s%k]+=1
                else:
                    dic[s%k]=1
        return count
        
