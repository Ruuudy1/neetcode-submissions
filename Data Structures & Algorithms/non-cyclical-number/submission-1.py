class Solution:

    def isHappy(self, n: int) -> bool:
        return self.helper(n, set())

    def helper(self, n, seen):
        if n == 1:
            return True
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        return self.helper(n, seen)