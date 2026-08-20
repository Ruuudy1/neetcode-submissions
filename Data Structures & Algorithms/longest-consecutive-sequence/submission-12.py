class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapped = sorted(set(nums))
        print(mapped)
        if not mapped:
            return 0
        current, longest = 1, 1
        for i in range(1, len(mapped)):
            if mapped[i] == mapped[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest