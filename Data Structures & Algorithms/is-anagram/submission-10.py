from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sset = set(s)
        # # Tset = set(t)

        return Counter(s) == Counter(t)