class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res =''
        for i,j in zip(strs[0],strs[len(strs)-1]):
            if i==j:
                res+=i
            else:
                return res
        return res
