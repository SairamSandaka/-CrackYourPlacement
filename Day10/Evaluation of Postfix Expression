class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, s):
        #code here
        st = []
        for i in s:
            if(i.isnumeric()):
                st.append(i)
            else:
                a = st.pop(len(st)-1)
                b = st.pop(len(st)-1)
                a = int(a)
                b = int(b)
                if(i=='+'):
                    st.append(b+a)
                elif(i=="-"):
                    st.append(b-a)
                elif(i=="*"):
                    st.append(b*a)
                else:
                    st.append(b//a)
        return st[0]
