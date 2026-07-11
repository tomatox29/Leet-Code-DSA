class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        new = [[0] * c for _ in range(r)]

        row = 0
        col = 0

        for i in range(m):
            for j in range(n):
                new[row][col] = mat[i][j]

                col += 1

                if col == c:
                    col = 0
                    row += 1

        return new