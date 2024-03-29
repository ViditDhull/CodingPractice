class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = False
        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zero_row = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(1, rows):
                matrix[r][0] = 0

        if zero_row:
            for c in range(cols):
                matrix[0][c] = 0