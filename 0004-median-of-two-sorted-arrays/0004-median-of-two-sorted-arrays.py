import statistics
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = np.concatenate((nums1, nums2))
        return float(statistics.median(merged))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        x = len(merged)
        if x % 2 == 1:
            return merged[x // 2]
        else:
            return (merged[x // 2 - 1] + merged[x // 2]) / 2.0
