class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        a = [[0]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                a[j][h-1-i]=matrix[i][j]
        for i in range(h):
            for j in range(w):
                matrix[i][j]=a[i][j]
