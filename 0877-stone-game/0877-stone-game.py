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

       #second method
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a = 0
        b = 0
        while piles:
            if piles[0] < piles[-1]:
                chosen = piles.pop(-1)  
            else:
                chosen = piles.pop(0) 
                
            if True:
                a += chosen
            else:
                b += chosen
            
        return a > b

            
        