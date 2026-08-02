class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a=0
        b=0
        for i, pile in enumerate(piles):
            if piles[i]<piles[-1]:
                a+=piles[-1]
                b+=piles[i]
                piles.pop(-1)
            else:
                a+=piles[i]
                piles.pop(i)
        return a>b
            
            
        