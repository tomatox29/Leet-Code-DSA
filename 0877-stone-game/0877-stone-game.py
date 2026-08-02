class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True 
        
        #two pointer 
        a=0
        b=0
        left=0
        right = len(piles)-1
        while left<=right:
            if piles[left]>piles[right]:
                chosen=piles[left]
                left+=1
            else:
                 chosen=piles[right]
                 right-=1
            if True:
                a+=chosen
            else:
                b+=chosen 
        return a>b 

       #second method (not good may caused index error)
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
            
            
        