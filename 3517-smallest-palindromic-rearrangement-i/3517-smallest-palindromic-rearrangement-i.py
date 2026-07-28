from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq={}
        freq=Counter(s)
        left =[]
        mid = ""
        for ch, count in freq.items():
            if count %2==1:
                mid=ch

            left+=[ch]*(count//2)
        left=sorted(left)
        right = left[::-1]

        return "".join(left) + mid + "".join(right)
            









 