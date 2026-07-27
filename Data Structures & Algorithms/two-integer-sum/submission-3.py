class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}#val:index
        ret = []

        for i, x in enumerate(nums):

            a = target - x

            if a in dict:
                ret.append(dict[a])
                ret.append(i)
                
            else:
                dict[x] = i

        return ret