class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         max1=max(nums)
#         nums.remove(max1)
#         max2=max(nums)
#         nums.remove(max2)
#         max3=max(nums)

#         return max1*max2*max3

