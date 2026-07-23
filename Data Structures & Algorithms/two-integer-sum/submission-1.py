class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = {}
        ret = []

        for i, x in enumerate(nums):
            dict[x] = target - x
            index[x] = i


        for i, x in enumerate(nums):
            temp = target - x
            if temp in index and index[temp] != i:
                ret.append(i)
                ret.append(index[temp])
                return sorted(ret)