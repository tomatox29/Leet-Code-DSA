class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start=min(nums)
        end=max(nums)
        set_nums=set(nums)
        return [x for x in range(start, end + 1) if x not in set_nums]

        #second solution same idea differnt style 
        nums.sort()
        ans=[]
        j=0
        for i in range(nums[0],nums[-1]):
            if nums[j]!=i:
                a.append(i)
            else:
                j+=1
        return ans



        