class Solution:
    def simplifyPath(self, path: str) -> str:
        files = []
        st = []
        s = ''
        for i in path:
            if(i=='/'):
                if len(s)>0: st.append(s)
                st.append('/')
                s = ''
            else:
                s+=i
        if(len(s)>0):
            st.append(s)
        print(st)
        count=0
        for i in st:
            if(i==".."):
                if len(files)>=2:
                    files.pop(len(files)-1)
                    files.pop(len(files)-1)
                else:
                    while(len(files)<=0):
                        files.pop(len(files)-1)
            elif(i=='.'):
                continue
            elif(i=='/'):
                if(count==0):
                    files.append("/")
                    count+=1
            else:
                files.append(i)
                count-=1
        if(files[-1]=='/' and len(files)>1):
            files.pop(-1)
        s = ''
        for i in files:
            s+=i
        return s
        
