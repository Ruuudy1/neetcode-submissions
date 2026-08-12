class Solution:
    RECURSION_COUNT = 0
    
    def isHappy(self, n: int) -> bool:
        self.RECURSION_COUNT += 1
        digits = [int(digit) ** 2 for digit in str(n)]
        if sum(digits) == 1:
            return True
        if self.RECURSION_COUNT > 993:
            return False
        count = sum(digits)
        return self.isHappy(count)