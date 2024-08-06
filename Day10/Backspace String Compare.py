class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in s:
            if(i=='#' ):
                if(s1):
                    s1.pop(len(s1)-1)
            else:
                s1.append(i)
        for i in t:
            if(i=='#'):
                if(s2):
                    s2.pop(len(s2)-1)
            else:
                s2.append(i)
        if(s1==s2):
            return True
        return False
        
