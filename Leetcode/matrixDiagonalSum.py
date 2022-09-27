class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n==1:
            return mat[0][0]
                   
        sum=0
        for i in range(n):
            if i!=n-i-1:
                sum+=mat[i][i]+mat[i][n-i-1]
            else:
                sum+=mat[i][i]
        return sum