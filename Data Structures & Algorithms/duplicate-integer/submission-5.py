class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) != len(nums))
        # dic = set()
        # for n in nums:
        #     if n in dic:
        #         return True            
        #     dic.add(n)
        # return False