from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * len(nums)
        groups = []
        
        for val, idx in sorted_pairs:
            if not groups or val - groups[-1][-1][0] > limit:
                groups.append([])
            groups[-1].append((val, idx))
            
        for group in groups:
            indices = sorted(idx for val, idx in group)
            for i, (val, idx) in enumerate(group):
                result[indices[i]] = val
                
        return result
