import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        prefixGcd=[]
        for num in nums:
            mx=max(mx,num)
            pfg=math.gcd(num,mx)
            prefixGcd.append(pfg)
        prefixGcd.sort()
        
        n=len(prefixGcd)
        left = 0
        right = n - 1
        ans=0
        while left<right:
            gcdx=math.gcd(prefixGcd[left], prefixGcd[right])
            ans+=gcdx
            left+=1
            right-=1

        return ans

        
            

        
 


            

        
    


        