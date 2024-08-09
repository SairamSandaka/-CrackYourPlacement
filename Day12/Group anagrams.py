class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            a = ''.join(sorted(i))
            if(a in dic):
                dic[a].append(i)
            else:
                dic[a]=[i]
        res = []
        for i in dic:
            res.append(dic[i])
        res.sort()
        return res
        
