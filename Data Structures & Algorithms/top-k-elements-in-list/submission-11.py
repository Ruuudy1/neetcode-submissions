class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result