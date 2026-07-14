from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        NUM_OF_ROWS, NUM_OF_COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_stage = 0
        stages = [deque()]
        rotten_locations = set()
        fresh_locations = set()
                

        for row in range(NUM_OF_ROWS):
            for col in range(NUM_OF_COLS):
                if grid[row][col] == ROTTEN:
                    stages[curr_stage].append((row, col))
                    rotten_locations.add((row, col))
                if grid[row][col] == FRESH:
                    fresh_locations.add((row, col))
        
        while curr_stage < len(stages):
            while stages[curr_stage]:
                row, col = stages[curr_stage].popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr >= 0 and nr < NUM_OF_ROWS) and (nc >= 0 and nc < NUM_OF_COLS) and ((nr, nc) not in rotten_locations) and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        if len(stages) == curr_stage + 1:
                            stages.append(deque())
                        stages[curr_stage + 1].append((nr, nc))
                        rotten_locations.add((nr, nc))
                        fresh_locations.remove((nr, nc))
                
            curr_stage += 1
        
        return -1 if fresh_locations else max(0, curr_stage - 1)