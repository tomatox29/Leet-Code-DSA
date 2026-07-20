class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k = k % total
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_flat_index = (i * n + j + k) % total
                new_row = new_flat_index // n
                new_col = new_flat_index % n
                
                result[new_row][new_col] = grid[i][j]
                
        return result
