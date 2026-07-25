class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(abs(n))] 
        max1,max2=-1,-1
        for d in digits:
            if d>max1:
                max2=max1
                max1=d
            elif d> max2:
                max2=d
        return max1*max2
  
        

       
            
        