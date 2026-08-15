class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor=0
        if all(x==0 for x in nums):
            return 0
        for num in nums:
            total_xor^=num

        if total_xor>0:
            return n
        return n-1 

        