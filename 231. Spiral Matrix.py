class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, right = 0, len(matrix[0])
        bottom, left = len(matrix), 0

        while top < bottom and left < right:
            # left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not( top < bottom and left < right):
                break
            
            # right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res