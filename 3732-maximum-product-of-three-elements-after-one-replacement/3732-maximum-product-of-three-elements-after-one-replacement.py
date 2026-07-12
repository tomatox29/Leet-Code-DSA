class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1,num2= nlargest(2,map(abs,nums))
        return num1 * num2 * 10**5
        



        