class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        while n!=0:
            if n&1==1:
                count+=1
            n>>=1
        return count 


        count = 0
        if n&n-1==0:
            return 1

        rest = bin(n)
        for bit in rest:
            if bit == 1:
                count+=1

        return count