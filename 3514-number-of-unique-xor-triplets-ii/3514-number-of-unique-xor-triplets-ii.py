class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        while ans <= max(nums):
            ans <<= 1

        pair_seen = [False] * ans

        for i in range(n):
            for j in range(i, n):
                pair_seen[nums[i] ^ nums[j]] = True

        triplet_seen = [False] * ans

        for pair_xor in range(ans):
            if pair_seen[pair_xor]:
                for num in nums:
                    triplet_seen[pair_xor ^ num] = True

        return sum(triplet_seen)