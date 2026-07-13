class Solution:
    def isUgly(self, n: int) -> bool:

        # Ugly numbers must be positive
        if n <= 0:
            return False

        # Remove all factors of 2, 3, and 5
        for x in [2, 3, 5]:

            # Keep dividing while n is divisible by x
            while n % x == 0:
                n //= x

        # If nothing except 1 remains, it is an ugly number
        return n == 1
        
        
        
