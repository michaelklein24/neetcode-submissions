class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        NUM_OF_ROWS, NUM_OF_COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or r < 0 or c < 0 or r == NUM_OF_ROWS or c == NUM_OF_COLS or heights[r][c] < prev_height):
                return
            visit.add((r,c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for c in range(NUM_OF_COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(NUM_OF_ROWS - 1, c, atlantic, heights[NUM_OF_ROWS - 1][c])
        
        for r in range(NUM_OF_ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, NUM_OF_COLS - 1, atlantic, heights[r][NUM_OF_COLS - 1])

        res = []
        for r in range(NUM_OF_ROWS):
            for c in range(NUM_OF_COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res

