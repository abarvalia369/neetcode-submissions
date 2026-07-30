class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        data = {}
        ctr = 0
        ret = []

        for x in nums:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
        largest = sorted(data.items(), key=lambda kv: kv[1], reverse = True)
        for x in largest:
            if ctr<k:
                ret.append(x[0])
            ctr += 1
        
        return ret

