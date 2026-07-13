class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            freq[ch]=freq.get(ch,0)-1
            

        # Find the extra character
        for key, value in freq.items():
            if value == -1:
                return key 
