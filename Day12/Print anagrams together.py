class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        dic = {}
        for i in words:
            a = ''.join(sorted(i))
            if(a in dic):
                dic[a].append(i)
            else:
                dic[a]=[i]
        res = []
        for i in dic:
            res.append(dic[i])
            
        return res
