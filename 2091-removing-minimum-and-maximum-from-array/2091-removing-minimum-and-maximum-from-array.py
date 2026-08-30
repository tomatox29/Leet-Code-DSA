class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return n 
        min_index=nums.index(min(nums))
        max_index=nums.index(max(nums))

        i=min(min_index,max_index)
        j=max(min_index,max_index)

        front=j+1
        back=n-i
        from_both=(i+1)+(n-j)
        return min(front,back,from_both)

        