class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
        for c in count:
            if count[c] == 1:
                return s.index(c)
        return -1