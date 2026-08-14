class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_counter = {}
        for i in range(len(nums)):
            if nums[i] in nums_counter:
                return True
            nums_counter[nums[i]] = nums_counter.get(nums[i], 0) + 1
        return False