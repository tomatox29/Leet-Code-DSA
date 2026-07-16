class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0
        window_sum = sum(nums[:k])
        mx = window_sum

        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            mx = max(window_sum, mx)
        return mx / k
