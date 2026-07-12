class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_count = 0
        
        for right in range(len(s)):
            # While the character is a duplicate, shrink window from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the new unique character to our window
            char_set.add(s[right])
            
            # Calculate current window size: (right - left + 1)
            max_count = max(max_count, right - left + 1)
            
        return max_count

        max_count=0
        stack=[]
        for ch in s:
            while ch in stack:
                stack.pop(0)
            stack.append(ch)
            max_count=max(max_count,len(stack))
        return max_count
        



            