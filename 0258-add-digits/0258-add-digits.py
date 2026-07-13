class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: 
            return num
        
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num
        
        
