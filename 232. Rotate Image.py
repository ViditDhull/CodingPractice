class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right- left):
                top, bottom = left, right
                
                # move leftmost to a temporary variable
                topleft = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                #move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move topright to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left to top right
                matrix[top + i][right] = topleft
            left += 1
            right -= 1
