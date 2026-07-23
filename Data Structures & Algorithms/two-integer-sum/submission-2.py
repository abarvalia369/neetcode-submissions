class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, n in enumerate(nums):
            temp = target - n
            if temp in dict:
                return [dict[temp],i]
            dict[n] = i
     