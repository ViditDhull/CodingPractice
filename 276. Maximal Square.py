class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mx=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]=="0"):
                    matrix[i][j]=0
                else:
                    if(i==0 or j==0):
                        matrix[i][j]=1
                    else:
                        matrix[i][j]=min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])+1
                mx=max(mx,matrix[i][j])
            # print(matrix[i])
        # print(matrix)
        return mx**2