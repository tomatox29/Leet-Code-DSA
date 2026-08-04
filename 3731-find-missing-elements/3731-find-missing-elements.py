class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start=min(nums)
        end=max(nums)
        set_nums=set(nums)
        return [x for x in range(start, end + 1) if x not in set_nums]



        