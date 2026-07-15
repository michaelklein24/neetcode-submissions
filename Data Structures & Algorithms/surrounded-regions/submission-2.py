class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIRECTIONS = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        NUM_OF_ROWS, NUM_OF_COLS = len(board), len(board[0])
        visited = set()
        regions = [] # List of sets (surrounded regions)
        contains_edge = False

        def dfs(r, c, region):
            nonlocal contains_edge
            if (r < 0 or r == NUM_OF_ROWS or c < 0 or c == NUM_OF_COLS or (r, c) in visited or board[r][c] == "X"):
                return
            
            visited.add((r, c))
            region.add((r, c))
            
            if r == 0 or r == NUM_OF_ROWS - 1 or c == 0 or c == NUM_OF_COLS - 1:
                contains_edge = True

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, region)
        
        for row in range(NUM_OF_ROWS):
            for col in range(NUM_OF_COLS):
                if (row, col) not in visited:
                    region = set()
                    dfs(row, col, region)
                    if region and not contains_edge:
                        regions.append(region)
                    contains_edge = False

        for region in regions:
            for row, col in region:
                board[row][col] = "X"
