class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        def dfs(sr, sc ):
            if sr > 0 and image[sr-1][sc] == original_color and image[sr-1][sc] != color:
                image[sr-1][sc] = color
                dfs(sr-1, sc)
            if sc > 0 and image[sr][sc-1] == original_color and image[sr][sc-1] != color:
                image[sr][sc-1] = color
                dfs(sr, sc-1)
            if sr < len(image) - 1 and image[sr+1][sc] == original_color and image[sr+1][sc] != color:
                image[sr+1][sc] = color
                dfs(sr+1, sc)
            if sc < len(image[0]) - 1 and image[sr][sc+1] == original_color and image[sr][sc+1] != color:
                image[sr][sc+1] = color
                dfs(sr, sc+1)
            return None
        
        if original_color != color:
            image[sr][sc] = color
        dfs(sr, sc)

        return image
