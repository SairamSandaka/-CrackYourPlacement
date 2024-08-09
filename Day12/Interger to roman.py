class Solution:
    def intToRoman(self, num: int) -> str:
        inte = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M",'CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        s = ''
        for i in range(len(inte)):
            while(num>=inte[i]):
                s+=sym[i]
                num-=inte[i]
        return s


