class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = dict()
        for i in range(len(nums)):
            if nums[i] in counter:
                return True
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        return False