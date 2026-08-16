class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for string in strs:
            count = [0] * 26 
            for char in string:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in result:
                result[key] = []
            result[tuple(count)].append(string)
        return list(result.values())
