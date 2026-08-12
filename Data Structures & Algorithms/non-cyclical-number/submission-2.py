class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            return sum(int(digit) ** 2 for digit in str(n))
        slow = n
        fast = helper(n)
        while fast != 1 and slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))
        return fast == 1

    # def isHappy(self, n: int) -> bool:
    #     return self.helper(n, set())

    # def helper(self, n, seen):
    #     if n == 1:
    #         return True
    #     if n in seen:
    #         return False
    #     seen.add(n)
    #     n = sum(int(digit) ** 2 for digit in str(n))
    #     return self.helper(n, seen)