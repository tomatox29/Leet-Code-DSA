class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_t = sum(ord(ch) for ch in t)
        sum_s = sum(ord(ch) for ch in s)

        return chr(sum_t-sum_s)





        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            freq[ch]=freq.get(ch,0)-1
        for key, value in freq.items():
            if value == -1:
                return key 


