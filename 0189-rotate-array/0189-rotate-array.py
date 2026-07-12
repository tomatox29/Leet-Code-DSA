class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[::-1]      
        nums[:k] = nums[:k][::-1]  
        nums[k:] = nums[k:][::-1]

        # second method
        # n=len(nums)
        # k %=n
        # doubled = nums + nums
        # nums[:] = doubled[n - k : n - k + n]




        