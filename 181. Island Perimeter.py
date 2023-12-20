class Solution(object):
    def islandPerimeter(self, grid):
        tp = 0
        lg = len(grid)
        count = 1
        for i in range(lg):
            for j in range(len(grid[i])):
                bp = 4
                if grid[i][j] == 1:
                    if len(grid[i]) > j + 1:
                        if grid[i][j+1] == 1:
                            bp -= 1
                    if j - 1 >= 0:
                        if grid[i][j-1] == 1:
                            bp -= 1
                    if len(grid) > i + 1:
                        if grid[i+1][j] == 1:
                            bp -= 1
                    if i - 1 >= 0:
                        if grid[i-1][j] == 1:
                            bp -= 1
                    tp += bp
        return tp