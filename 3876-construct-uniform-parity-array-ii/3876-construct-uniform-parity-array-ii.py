class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        evens=[x for x in nums1 if x %2==0]
        odds=[x for x in nums1 if x %2!=0]
        
        if not evens or not odds:
            return True
        return min(odds)<min(evens)

    