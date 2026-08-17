class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in counter:
                return [counter[complement], i]
            counter[n] = i