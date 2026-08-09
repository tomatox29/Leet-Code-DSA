from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, min(2 * M, n - i) + 1):
                taken = suffix[i] - suffix[i + X]

                best = max(
                    best,
                    suffix[i] - dp(i + X, max(M, X))
                )

            memo[(i, M)] = best
            return best

        return dp(0, 1)

