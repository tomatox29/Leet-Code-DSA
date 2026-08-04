class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        numbers=list(range(min(nums),max(nums)))
        result = [num for num in numbers if num not in nums]
        return result 


        