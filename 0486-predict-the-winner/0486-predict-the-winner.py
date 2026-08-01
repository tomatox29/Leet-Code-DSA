class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=list(nums)
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if i==j:
                    return True 
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] >= 0


