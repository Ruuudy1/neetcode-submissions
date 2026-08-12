from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = sorted(s)
        tSet = sorted(t)

        if len(s) is not len(t):
            return False
            
        for i in range(len(s)):
            if sSet[i] is not tSet[i]:
                return False
        return True

        
