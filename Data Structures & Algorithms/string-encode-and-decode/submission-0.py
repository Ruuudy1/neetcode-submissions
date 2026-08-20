class Solution:

    def encode(self, strs: List[str]) -> str:
        result: str = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result: List[str] = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j+1+length
        return result