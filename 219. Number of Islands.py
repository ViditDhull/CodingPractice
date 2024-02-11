class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] != '0':
                    self.visit_island(grid, x, y)
                    islands += 1
        return islands
    
    def visit_island(self, grid, x, y):
        xlen = len(grid)
        ylen = len(grid[0])
        grid[x][y] = '0'
        #x down
        if x > 0 and grid[x-1][y] != '0' and (x-1, y):
            self.visit_island(grid, x - 1, y)
        #x up
        if x < xlen - 1 and grid[x+1][y] != '0' and (x+1, y):
            self.visit_island(grid, x + 1, y)
        #y up
        if y > 0 and grid[x][y-1] != '0' and (x, y-1):
            self.visit_island(grid, x, y - 1)
        #y down
        if y < ylen - 1 and grid[x][y+1] != '0' and (x, y+1):
            self.visit_island(grid, x, y + 1)
        