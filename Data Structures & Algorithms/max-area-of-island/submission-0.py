class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(r: int, c: int) -> int:
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0 or (r, c) in visited):
                return 0 
            
            visited.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        for row in range(ROWS):
            for col in range(COLS):
                area = dfs(row, col)
                result = max(result, area)
        
        return result