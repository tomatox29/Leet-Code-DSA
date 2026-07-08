class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        missing = []

        for i in range(1, len(nums) + 1):
            if i not in s:
                missing.append(i)

        return missing