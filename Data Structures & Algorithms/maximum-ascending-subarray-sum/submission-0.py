class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                curr = nums[i]
            result = max(result, curr)
        return result