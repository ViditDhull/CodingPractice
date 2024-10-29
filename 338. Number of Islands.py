class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ni = 0
        def dfs(r,c):
            grid[r][c] = 2
            if r > 0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            if c > 0 and grid[r][c-1] == '1':
                dfs(r, c-1)
            if r < len(grid) - 1 and grid[r+1][c] == '1':
                dfs(r+1, c)
            if c < len(grid[0]) - 1 and grid[r][c+1] == '1':
                dfs(r, c+1)
            return None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    ni += 1
                    dfs(r, c)

        return ni
