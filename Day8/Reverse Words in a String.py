class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        r = ''
        for i in s:
            if(i!=" "):
                r+=i
            elif(i == " " and r!=''):
                l.append(r)
                r = ''
        if(r!='' and r!=' '):
            l.append(r)
        print(l)
        res = ''
        for i in l[::-1]:
            res+=i+" "
        return res[:-1]
                
