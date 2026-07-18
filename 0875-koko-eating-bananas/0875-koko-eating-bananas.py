class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for pile in piles:
                hours = (pile + mid - 1) // mid
                total+= hours
                pass
            if total <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid+1

        return ans