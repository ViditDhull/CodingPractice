class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = 0
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] > target:
                break
            else:
                row_index = i

        for i in range(len(matrix[0])):
            if matrix[row_index][i] == target:
                return True
        return False
