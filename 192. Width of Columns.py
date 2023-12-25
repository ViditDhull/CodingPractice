class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        lg = len(grid)
        result = []
        for j in range(len(grid[0])):
            mw = 0
            for i in range(lg):
                if len(str(grid[i][j])) > mw:
                    mw = len(str(grid[i][j]))
            result.append(mw)
        return result