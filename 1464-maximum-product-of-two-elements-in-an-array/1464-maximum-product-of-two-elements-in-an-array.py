class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove (max1)
        max2 = max(nums)
        return (max1-1)*(max2-1)


#second approach 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = 0
        for i in range(1, len(nums)):
            for j in range( len(nums)):
                if i!=j:
                    max_value=max((nums[i]-1)*(nums[j]-1),max_value)

        return max_value 


