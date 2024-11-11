from typing import List

class Solution:
    def getTotalIsles(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfsc(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            visited[r][c] = True
            dfsc(r + 1, c)  # Down
            dfsc(r - 1, c)  # Up
            dfsc(r, c + 1)  # Right
            dfsc(r, c - 1)  # Left

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1

        return island_count