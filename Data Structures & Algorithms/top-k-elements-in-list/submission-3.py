class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        data = {}
        ctr = 0
        ret = []
        a = len(nums)+1
        ary = [[] for _ in range(a)]
        print(nums)
        for x in nums:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
        print(data)
        for x in data.items():            
            ary[x[1]].append(x[0])
            print(ary)

        for x in reversed(ary):
            if x != [] and ctr < k:
                for i in x:
                    print(i)
                    ret.append(i)
                    print(ret)
                    ctr += 1
                    print(ctr)
            
        return ret

