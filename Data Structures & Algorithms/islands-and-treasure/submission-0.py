from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_of_rows, num_of_cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = deque([(row, col, 0)])
            visited = {(row, col)}

            while queue:
                row, col, dist = queue.popleft()

                if grid[row][col] > 0:
                    grid[row][col] = min(grid[row][col], dist)

                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                ]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < num_of_rows
                        and 0 <= nc < num_of_cols
                        and grid[nr][nc] != -1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))

        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if grid[row][col] == 0:
                    bfs(row, col)