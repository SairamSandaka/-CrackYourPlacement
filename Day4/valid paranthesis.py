class Solution:
    def isValid(self, s: str) -> bool:
        l =[]
        for i in s:
            if(i=='{' or i=='(' or i=='['):
                l.append(i)
            elif((i=='}' or i==']' or i==')') and len(l)==0):
                return False
            elif((i==')' and l[len(l)-1]=='(') or (i==']' and l[len(l)-1]=='[') or (i=='}' and l[len(l)-1]=='{')):
                l.pop()
            else:
                l.append(i)
            
                
        if(len(l)==0):
            return True
        else:
            return False
        
