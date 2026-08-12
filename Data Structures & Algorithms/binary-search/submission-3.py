class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            match m:
                case m if nums[m] == target:
                    return m
                case m if nums[m] < target:
                    l = m + 1
                case m if nums[m] > target: 
                    r = m - 1
        return -1

