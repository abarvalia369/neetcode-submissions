class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash = set()

        for x in range(len(nums)):
            if nums[x] in hash:
                return True
            hash.add(nums[x])
        return False