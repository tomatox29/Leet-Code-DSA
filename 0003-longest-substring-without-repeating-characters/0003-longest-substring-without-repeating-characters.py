class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        stack=[]
        for ch in s:
            while ch in stack:
                stack.pop(0)
            stack.append(ch)
            max_count=max(max_count,len(stack))
        return max_count
        



            