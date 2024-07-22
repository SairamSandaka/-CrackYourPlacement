class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        st = []
        n = columnNumber
        while(n>0):
            if(n%26==0):
                st.append(26)
            else:
                st.append(n%26)
            if(n%26==0):
                n-=1
            n = n//26
        res=''
        for i in st[::-1]:
            res+=chr(i+64)
        return res
        
