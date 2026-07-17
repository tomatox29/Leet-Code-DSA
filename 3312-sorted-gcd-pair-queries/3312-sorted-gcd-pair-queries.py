from bisect import bisect_left
from typing import List
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m=max(nums)
        cnt = [0] * (m + 1)
        for num in nums:
            cnt[num] += 1
        gcdCount = [0] * (m + 1)
        for i in range(m,0,-1):
            div=0
            for j in range(i,m+1,i):
                div+=cnt[j]
            pairs = div * (div - 1) // 2
            gcdCount[i] = pairs
            for k in range(i*2,m+1,i ):
                gcdCount[i] -= gcdCount[k]
        for i in range(1, m + 1):
            gcdCount[i] += gcdCount[i - 1]
        ans=[] 
        for q in queries:
            ans.append(bisect_left(gcdCount, q + 1))
        return ans

