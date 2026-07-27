class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(set(nums))
        return a != len(nums)