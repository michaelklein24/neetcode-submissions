from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_id = 0
        found = set() # 'row:col'
        islands = defaultdict(set)

        def discover_island(row: int, col: int, island: set) -> set:
            if grid[row][col] != "1" or f"{row}:{col}" in found:
                return island

            island.add(f"{row}:{col}")

            left = (row - 1, col) if row > 0 else None
            right = (row + 1, col) if row < len(grid) - 1 else None
            top = (row, col - 1) if col > 0 else None
            bottom = (row, col + 1) if col < len(grid[0]) - 1 else None
            
            if left and f"{left[0]}:{left[1]}" not in island:
                island = island.union(discover_island(left[0], left[1], island))
            if right and f"{right[0]}:{right[1]}" not in island:
                island = island.union(discover_island(right[0], right[1], island))
            if top and f"{top[0]}:{top[1]}" not in island:
                island = island.union(discover_island(top[0], top[1], island))
            if bottom and f"{bottom[0]}:{bottom[1]}" not in island:
                island = island.union(discover_island(bottom[0], bottom[1], island))
            
            return island
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                land = grid[row][col]
                if land not in found:
                    island = discover_island(row, col, set())
                    if island:
                        found = found.union(island)
                        islands[f"{row}:{col}"] = island

        return len(islands.keys())