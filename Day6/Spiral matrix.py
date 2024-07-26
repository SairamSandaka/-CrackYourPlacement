class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        size = m*n
        res = []
        up = 0
        left = 0 
        right = n-1
        down = m-1
        while(len(res)<size):
            i=left
            while(i<right+1 and len(res)<size):
                res.append(matrix[up][i])
                i+=1
            up+=1
            i = up
            while(i<down+1 and len(res)<size):
                res.append(matrix[i][right])
                i+=1
            right-=1
            i = right
            while(i>left-1 and len(res)<size):
                res.append(matrix[down][i])
                i-=1
            down-=1
            i = down
            while(i>up-1 and len(res)<size):
                res.append(matrix[i][left])
                i-=1
            left+=1
        return res


