class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        counts = list(freq.values())
        counts.sort(reverse=True)
        ans = 0
        for i, f in enumerate(counts):
            ans+=f* (i//8+1)
        return ans 

        
        