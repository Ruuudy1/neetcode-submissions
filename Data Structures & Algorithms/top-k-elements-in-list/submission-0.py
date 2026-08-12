from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tupleList = list(Counter(nums).most_common(k))
        return [x[0] for x in tupleList]