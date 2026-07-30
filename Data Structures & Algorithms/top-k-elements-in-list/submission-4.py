class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        data = {}
        ctr = 0
        ret = []
        a = len(nums)+1
        ary = [[] for _ in range(a)]
        #^bad in this small input size because allocatedint 100,001 lists and only using 200
        for x in nums:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
        for x in data.items():            
            ary[x[1]].append(x[0])

        for x in reversed(ary):
            if x != [] and ctr < k:
                for i in x:
                    ret.append(i)
                    ctr += 1
            
        return ret

#O(n)